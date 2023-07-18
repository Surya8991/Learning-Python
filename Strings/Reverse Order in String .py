# Program to reverse the order of words in string
def revese_order(str):
    words=str.split()
    reversed_word=" ".join(words[::-1])
    return reversed_word

# inputs
print(revese_order("Hello World"))