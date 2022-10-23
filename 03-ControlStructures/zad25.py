# 25.	The variables a and b contain the dimensions of the sides of the rectangle. 
# Write a program that creates the following rectangle with dimensions a and b. 

rows = int(input("a = "))
columns = int(input("b = "))

for i in range(rows):
    for j in range(columns):
        if(i == 0 or i == rows - 1 or j == 0 or j == columns - 1):
            print('*', end = '  ')
        else:
            print(' ', end = '  ')
    print()