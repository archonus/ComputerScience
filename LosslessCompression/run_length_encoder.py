
def rle_encode(data):
    """
    Basic run-length encoding of data
    :param data: The string to be encoded
    :return: The encoded string
    """
    encoding = ''
    prev_char = ''
    count = 1

    if not data: return '' #Data is an empty string itself

    for char in data:
        # If the prev and current characters
        # don't match...
        if char != prev_char:
            # ...then add the count and character
            # to our encoding
            if prev_char != '': #It isn't the start of the string
                encoding += str(count) + prev_char
            count = 1
            prev_char = char
        else:
            # Or increment our counter
            # if the characters do match
            count += 1
    else:
        # Finish off the encoding
        encoding += str(count) + prev_char
        return encoding


def rle_decode(encoded):
    decode = ''
    count = ''
    for char in encoded:
        # If the character is numerical...
        if char.isdigit():
            # ...append it to our count
            count += char
        else:
            # Otherwise we've seen a non-numerical
            # character and need to expand it for
            # the decoding
            decode += char * int(count)
            count = ''
    return decode


if __name__ == "__main__":
    choice = input("Do you wish to encode (e) or decode (d)...")
    if choice == "e":
        data = input("Please enter the input_string...")
        encoded = rle_encode(data)
        print(encoded)
    elif choice == "d":
        encoded = input("Please enter the encoded data...")
        decoded = rle_decode(encoded)
        print(decoded)
    else: print("Invalid input_string")
    input("Press enter to exit...")