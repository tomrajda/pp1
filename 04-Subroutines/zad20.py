# 20.	Define a function power(x, n) that evaluates x^n. Apply recursion. 
# Then calculate 5^3.

def power(x, n):
    """
    Returns power of number
    Applyinh recursion
    """
    if x == 1:
        return 1
    else:
        return x * (x ** (n-1))

print(power(2, 3))