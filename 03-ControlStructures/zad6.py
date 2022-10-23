# 6.	The speed limit on the motorway is 130 km / h. 
# Write a program that checks whether a car exceeded
# the speed limit.

limit = 130

# Checking if the speed is correct
if int(input("Type speed: ")) > limit:
    print("Speed exceeded!")
else:
    print("Speed is correct.")