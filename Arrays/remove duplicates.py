# remove duplicate elements in array
def duplicate_array(arr):
    dup_arr=[]
    for num in arr:
        if num not in dup_arr:
            dup_arr.append(num)
    return dup_arr

# inputs
print(duplicate_array([1,1,2,4,3,5,3]))