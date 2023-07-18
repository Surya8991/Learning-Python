# Program to find the sum of digits in a number

def sum_of_digits(n):
    sum=0
    while n > 0:
        sum += n%10
        n //=10
    return sum

# inputs
print(sum_of_digits(1234))