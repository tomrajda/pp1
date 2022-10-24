# 18.	Define a function that calculates the sum of number digits. 
# Then use the function to calculate the sum of digits in the number 7182.

def numbersSum(number):
    """
    Calculates the sum of number
    digits
    """
    sum = 0
    for i in str(number):
        sum += int(i)
    return sum

print(numbersSum(7182))
