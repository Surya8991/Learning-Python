# Program to print the array in Descending order

def ascending_order(arr):
    sorted_list=arr[:]
    for i in range(len(sorted_list)):
        for j in range(i+1,len(sorted_list)):
            if sorted_list[j] > sorted_list[i]:
                sorted_list[i],sorted_list[j]=sorted_list[j],sorted_list[i]
    return sorted_list

# input
print(ascending_order([1,95,5,3,54]))