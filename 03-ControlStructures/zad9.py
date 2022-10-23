# 9.	A user enters two integer numbers from the keyboard. 
# Write a program that checks if at least one of them is positive.


# User inpt
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

# Checking if at least one entered number is positive
if num1 > 0 or num2 > 0:
    print("One of numbers is positive.")
else:
    print("None of the numbers is positive.")