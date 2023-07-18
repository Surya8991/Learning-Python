def second_largest(arr):
    largest = max(arr[0], arr[1])
    second_largest_num = min(arr[0], arr[1])
    for i in range(2, len(arr)):
        if arr[i] > largest:
            second_largest_num = largest
            largest = arr[i]
        elif arr[i] > second_largest_num:
            second_largest_num = arr[i]
    return second_largest_num


print(second_largest([1, 2, 3, 4, 5]))
