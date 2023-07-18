# Program to find the 1st non repeatative in a string

def non_rep_str(str):
    char_count = {}
    for char in str:
        char_count[char] = char_count.get(char, 0)+1
    non_repeated = None
    for char in str:
        if char_count[char] == 1:
            non_repeated = char
            break
    return non_repeated

# input
print(non_rep_str("abacabad"))
    