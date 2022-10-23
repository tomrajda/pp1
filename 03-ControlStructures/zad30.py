# 30.	A natural number greater than 1 is called a prime if it has exactly 2 
# natural factors with the values 1 and this number. Write a program that finds 
# N leading prime numbers. Read the value of N from the keyboard. Using loop 
# statements check that the number N is divisible only by 1 and by N.

def isPrime(n):
    """
    Checking if the n
    is prime number
    """
    # check if the value is 2 (exception)
    if n == 2:
        return True
    # check if the value is even number or lower or equal than 1
    if n % 2 == 0 or n <= 1:
        return False
    # check if the value has any dividor
    e = int(n**0.5) + 1
    for i in range(3, e, 2):
        if n % i == 0:
            return False

    return True

# Data input, enter range
n = int(input())

print("Prime numbers:", end=" ")

# Checking all range of input
for i in range(n+1):
    if isPrime(i):
        print(i, end=" ")



