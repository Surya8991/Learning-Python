def freq_array(arr):
    freq={}
    for num in arr:
        if num in freq:
            freq[num] += 1
        else:
            freq[num]=1
    return freq

# Inputs
result=freq_array([1,4,5,1,5,58,5,6])

for char , count in result.items():
    print(f"{char}: {count}")
    