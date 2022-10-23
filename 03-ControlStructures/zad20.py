# 20.	Write a program that creates a multiplication table 
# in the range 1 to 10 for any number entered by the user

num = int(input("Enter number: "))
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")
