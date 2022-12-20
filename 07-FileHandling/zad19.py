# 19.	Create a program that writes to a text file integer numbers in the 
# range of <1,50>, every number in a separate line.

with open("int_numbers.txt", "w") as file:
    for i in range(1, 51):
        file.writelines(str(i) + "\n")

