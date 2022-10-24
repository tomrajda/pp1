def sum(n):
    """
    Returns sum in range
    (1, n)
    """
    if n <= 1:
        return n
    else:    
        return n + sum(n - 1)

num = 10

if num < 0:
   print("Enter a positive number")
else:
   print("The sum is", sum(num)) 