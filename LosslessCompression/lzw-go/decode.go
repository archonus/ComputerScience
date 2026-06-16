package main

import (
	"bytes"
	"encoding/binary"
	"fmt"
	"io"
)

type decodeEntry struct {
	prefix    uint16
	suffix    byte
	hasPrefix bool
}

func newDecodeDictionary() map[uint16]decodeEntry {
	dict := make(map[uint16]decodeEntry, 256)

	for i := 0; i < 256; i++ {
		dict[uint16(i)] = decodeEntry{
			suffix:    byte(i),
			hasPrefix: false,
		}
	}

	return dict
}

func expand(
	dict map[uint16]decodeEntry,
	code uint16,
	scratch []byte,
) ([]byte, byte, error) {
	// expand reconstructs the byte sequence represented by code.
	//
	// Dictionary entries point from their final byte to their prefix, so the
	// bytes are initially collected in reverse order. scratch is reused between
	// calls to avoid allocating a new slice for every decoded code.
	scratch = scratch[:0]

	for {
		entry, found := dict[code]
		if !found {
			return nil, 0, fmt.Errorf(
				"code %d is not in the dictionary",
				code,
			)
		}

		scratch = append(scratch, entry.suffix)

		if !entry.hasPrefix {
			break
		}

		code = entry.prefix
	}

	// The last collected byte is the first byte of the decoded sequence.
	firstByte := scratch[len(scratch)-1]

	// Reverse the sequence into output order.
	for left, right := 0, len(scratch)-1; left < right; left, right = left+1, right-1 {
		scratch[left], scratch[right] = scratch[right], scratch[left]
	}

	return scratch, firstByte, nil
}

func decode(codes []uint16) ([]byte, error) {
	if len(codes) == 0 {
		return nil, nil
	}

	const dictionarySize = 1 << 16

	var result bytes.Buffer

	// Reused while reconstructing dictionary entries.
	scratch := make([]byte, 0, 256)

	position := 0

	// Each outer-loop iteration represents one dictionary cycle.
	for position < len(codes) {
		dict := newDecodeDictionary()
		next := 256

		// The first code after initialisation or reset must be one of
		// the initial one-byte entries.
		firstCode := codes[position]
		if firstCode >= 256 {
			return nil, fmt.Errorf(
				"invalid first code %d at position %d after dictionary reset",
				firstCode,
				position,
			)
		}

		ret, _, err := expand(dict, firstCode, scratch)
		if err != nil {
			return nil, fmt.Errorf(
				"expanding code at position %d: %w",
				position,
				err,
			)
		}

		result.Write(ret)
		prevCode := firstCode
		position++

		for position < len(codes) {
			code := codes[position]

			var firstByte byte

			if int(code) < next { // Proxy for code being in dict.
				ret, first, err := expand(dict, code, scratch)
				if err != nil {
					return nil, fmt.Errorf(
						"expanding code at position %d: %w",
						position,
						err,
					)
				}

				result.Write(ret)
				firstByte = first
			} else {
				// The only valid missing code is the entry that the
				// encoder has just constructed: code == next.
				if int(code) != next {
					return nil, fmt.Errorf(
						"invalid code %d at position %d: next code is %d",
						code,
						position,
						next,
					)
				}

				// The special entry is:
				//
				//     previous sequence + first byte of previous sequence
				//
				// Output the previous sequence and then its first byte.
				ret, first, err := expand(dict, prevCode, scratch)
				if err != nil {
					return nil, fmt.Errorf(
						"expanding previous code at position %d: %w",
						position,
						err,
					)
				}

				result.Write(ret)
				result.WriteByte(first)
				firstByte = first
			}

			// Add:
			//
			//     previous sequence + first byte of current sequence
			//
			// Only the previous code and final byte need to be stored.
			dict[uint16(next)] = decodeEntry{
				prefix:    prevCode,
				suffix:    firstByte,
				hasPrefix: true,
			}

			// In the special case, code == next and the entry has now
			// been added, so code is also a valid previous code.
			prevCode = code

			next++
			position++

			if next == dictionarySize {
				// Code 65535 has just been added. The encoder continues
				// until its next attempted dictionary addition, then
				// resets. Because the decoder is one entry behind, the
				// next encoded code begins a new dictionary cycle here.
				break
			}
		}
	}

	return result.Bytes(), nil
}

func read(in io.Reader) ([]uint16, error) {
	var codes []uint16
	var buf [2]byte

	for {
		n, err := io.ReadFull(in, buf[:])

		switch {
		case err == nil:
			codes = append(
				codes,
				binary.LittleEndian.Uint16(buf[:]),
			)

		case err == io.EOF && n == 0:
			// Normal end of input.
			return codes, nil

		case err == io.ErrUnexpectedEOF:
			return nil, fmt.Errorf(
				"truncated code stream: expected 2 bytes, got %d",
				n,
			)

		default:
			return nil, fmt.Errorf("reading code stream: %w", err)
		}
	}
}
