# Program to find the number of occurunces of a word in a string
def word_occurence(str,word):
    count=0
    str=str.lower()
    words=str.split()
    for w in words:
        if w == word:
            count += 1
    return count

# inputs
print(word_occurence("she sells seashells by the sea shores","seashells"))