# Check if the String is palindrome or not

def str_is_palindrome(str):
    left = 0
    right = len(str)-1
    while left < right:
        if str[left] != str[right]:
            return False
        left += 1
        right -= 1
        return True
    # or
    # return str == str[::-1]


# input
result = str_is_palindrome("radar")
if (result):
    print("Palindrome")
else:
    print("Not a Palindrome")
