def find_max(arr):
  max_num = 0
  for num in arr:
    if num > max_num:
      max_num = num
  return max_num


print(find_max([1, 45, 848, 84, 47]))
