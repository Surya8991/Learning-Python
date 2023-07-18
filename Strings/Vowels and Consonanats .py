# Count the number of Vowels and consonants i String
def vowels_consonants(str):
    vowels_count=0
    cons_count=0
    vowels="aeiou"
    str=str.lower()
    for char in str:
        if char in vowels:
            vowels_count +=1
        else:
            cons_count += 1
    return vowels_count,cons_count

# inputs 
vowels,consonent=vowels_consonants("Apple")
print("Vowels: ",vowels)
print("Consonents: ",consonent)