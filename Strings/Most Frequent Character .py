def most_freq(str):
    char_count = {}  # Initialize as an empty dictionary
    for char in str:
        char_count[char] = char_count.get(char, 0) + 1

    max_char_no = 0
    most_freq_char = None
    for char, count in char_count.items():  # Use items() to iterate through the dictionary
        if count > max_char_no:
            max_char_no = count
            most_freq_char = char
    return most_freq_char

# input
print(most_freq("abradabra"))
