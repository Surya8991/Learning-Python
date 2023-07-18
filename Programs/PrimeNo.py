# Program to find if the number is a prime no. or not

def is_prime(num):
    if num < 2:
        return False
    for i in range(2,int(num**0.5)+1):
        if num % i == 0:
            return False
    return True

# inputs
print(is_prime(18))