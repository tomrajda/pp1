# 14.	An array contains values: [[True,False],[True,True],[False,False]]. 
# Create a program that changes values of an array to the opposite. 
# Use a loop statement.

arr = [[True,False],[True,True],[False,False]]

for i in range(len(arr)):
    for j in range(len(arr[i])):
        arr[i][j] = not arr[i][j]

print(arr)
