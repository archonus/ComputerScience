package main

import (
	"bytes"
	"encoding/base64"
	"encoding/binary"
	"fmt"
	"io"
)

type encodeKey struct {
	prefix uint16
	suffix byte
}

func newEncodeDictionary() map[encodeKey]uint16 {
	// Single-byte entries 0–255 are implicit.
	return make(map[encodeKey]uint16)
}

func encode(data []byte) []uint16 {
	if len(data) == 0 {
		return nil
	}

	const dictionarySize = 1 << 16

	dict := newEncodeDictionary()
	next := 256

	codes := make([]uint16, 0)

	// A one-byte sequence has the same code as the byte value.
	prevCode := uint16(data[0])

	for _, b := range data[1:] {
		// Is sequence represented by prevCode + byte b is already in the dictionary.
		key := encodeKey{
			prefix: prevCode,
			suffix: b,
		}

		if code, found := dict[key]; found {
			// The extended sequence already exists, so continue
			// accumulating input using its code.
			prevCode = code
			continue
		}

		// prevCode represents the longest sequence currently present
		// in the dictionary.
		codes = append(codes, prevCode)

		if next < dictionarySize {
			// Add:
			//
			//     sequence represented by prevCode + byte b
			//
			// without storing or copying the complete sequence.
			dict[key] = uint16(next)
			next++
		} else {
			// The complete uint16 code space has been used.
			// Reset to the implicit 256 one-byte entries.
			dict = newEncodeDictionary()
			next = 256
		}

		// Start a new sequence with the byte that could not be
		// appended to prevCode.
		prevCode = uint16(b)
	}

	// Emit the final accumulated sequence.
	codes = append(codes, prevCode)

	return codes
}

func write(out io.Writer, codes []uint16) error {
	var b [2]byte

	for _, code := range codes {
		binary.LittleEndian.PutUint16(b[:], code)

		n, err := out.Write(b[:])
		if err != nil {
			return fmt.Errorf("writing code stream: %w", err)
		}
		if n != len(b) {
			return io.ErrShortWrite
		}
	}

	return nil
}

func encodeBase64(text string) (string, error) {
	// []byte(text) produces the UTF-8 bytes of the Go string.
	codes := encode([]byte(text))

	var compressed bytes.Buffer

	if err := write(&compressed, codes); err != nil {
		return "", err
	}

	return base64.StdEncoding.EncodeToString(compressed.Bytes()), nil
}
