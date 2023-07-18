# Program to find the Fibonacci series
def fibonacci(n):
    sequence=[0,1]
    for i in range(2,n):
        sequence.append(sequence[i-1]+sequence[i-2])
    return sequence

# input
print(fibonacci(50))