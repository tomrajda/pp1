# 21. Search he Internet and familiarise yourself with RPN (Reverse Polish 
# Notation). Then, write a program that calculates RPN expressions. RPN can 
# be conveniently evaluated using a stack structure. A user can enter by the 
# keyboard any number, an operator (+ - * / ) or the equal sign (=).

#   a.	If the entered value is a number, push the number on to the stack
#   b.	If the entered value is an operator, pop two items from the top of 
#       the stack, do the calculation, and push the result of the operation 
#       on to the stack.
#   c.	If the entered value is an equal sign, pop the final result from the 
#       stack and display the result of calculation.

# Using the program, calculate the value of RPN expressions:

import stack

expression = input("Enter expression: ").split()

for value in expression:

    if value != "=":
        
        try:

            value_stack = int(value)
            stack.push(value_stack)

        except ValueError:

            value1 = stack.pop()
            value2 = stack.pop()

            if value == "+": 
                value_stack = value2 + value1
                stack.push(value_stack)

            elif value == "-":
                value_stack = value2 - value1
                stack.push(value_stack)

            elif value == "*":
                value_stack = value2 * value1
                stack.push(value_stack)

            elif value == "/":
                value_stack = value2 / value1
                stack.push(int(value_stack))

            elif value == "^":
                value_stack = value2 ** value1
                stack.push(int(value_stack))

    else:
        
        stack.display()