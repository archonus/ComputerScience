def encode(input_string, window_size = -1):
    current_index = 0
    if window_size == 0:
        raise ValueError("Window size cannot be 0")
    output = ""
    input_buffer = ""
    while current_index < len(input_string):
        if window_size < 0:
            input_buffer = input_string[:current_index]
        elif current_index - window_size > 0:
            input_buffer = input_string[current_index - window_size: current_index]
        else:
            input_buffer = input_string[:current_index]

        read = 0
        off_set = 0
        current_index += 1



if __name__ == "__main__":
    test_string = "ababcccdab"
    encode(test_string)
    input("Press enter to exit...")