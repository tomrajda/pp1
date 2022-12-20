# 14.	Write a program that calculates the number of lines for any text file. 
# The user enters the name of the file from the keyboard. Display the result 
# of the calculation (the file name and the number of lines). Do not display 
# the contents of the file. Sample result:
# File name: countries.txt
# Number of lines: 14

filename = input("Please enter file name: ") + ".txt"
with open(filename, "r") as file:
    counter = 0
    for i in file:
        counter += 1

print(f"File name: {filename}\nNumber of lines: {counter}")