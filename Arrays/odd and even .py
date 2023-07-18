# find the number of odd and even numbers in array

def odd_or_even_array(arr):
    even_count = 0
    odd_count = 0
    for num in arr:
        if num % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
    return even_count, odd_count


even, odd = odd_or_even_array([1, 2, 3, 4, 5])
print("Even Numbers : ", even)
print("Odd Numbers : ", odd)
