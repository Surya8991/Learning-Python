def avg_of_array(arr):
  avg_num = 0
  sum_num = 0
  for num in arr:
    sum_num += num
  avg_num = sum_num / len(arr)
  return avg_num


print(avg_of_array([1, 2, 3, 4, 5]))
