# Common elements in both array
def common_array(arr1,arr2):
    common_element=[]
    for num in arr1:
        if num in arr2 not in common_element:
            common_element.append(num)
    return common_element

# inputs
print(common_array([1,2,3,4,5],[5,9,6,3,1]))