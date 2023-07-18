def reverse_array(arr):
  # left = 0
  # right = len(arr) - 1
  # while left < right:
  #   temp = arr[left]
  #   arr[left] = arr[right]
  #   arr[right] = temp
  #   left += 1
  #   right -= 1
  # return arr
  # or

  length = len(arr)

  for i in range(length // 2):
    arr[i], arr[length - i - 1] = arr[length - i - 1], arr[i]
  return arr


print(reverse_array([1, 2, 3, 4, 5]))
