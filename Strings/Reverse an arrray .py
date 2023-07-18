# Reverse an array
def revese_string(str):
    # easy
    # revesed_string=reversed(str)
    reverseString = " "
    for char in str:
        reverseString = char + reverseString
    return reverseString


# inputs
print(revese_string("Hello"))
