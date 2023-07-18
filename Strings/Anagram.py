def are_anagrams(element1, element2):
    element1 = element1.lower().replace(" ", "")
    element2 = element2.lower().replace(" ", "")
    
    if sorted(element1) == sorted(element2):
        return True
    else:
        return False

# inputs
result = are_anagrams("silent", "listen")
if result:
    print("Anagram")
else:
    print("Not an Anagram")
