# 20.	Write a program that converts any natural number to a binary number. 
# Use the stack. To convert a number, divide the number by 2, each time taking 
# the remainder of the division and putting the remainder on the stack. Repeat 
# the division until the number you are dividing is zero. Then pop and display 
# all values from the stack. Sample result for number 18:

import stack

value = 25
print(f"Natural number: {value}")

while value != 0:

    result = value // 2

    if value % 2 == 0:
        stack.push(0)
    else:
        stack.push(1)

    value = result

print(f"Binary number: ", end="")
while not stack.empty():
    print(stack.pop(), end="")
