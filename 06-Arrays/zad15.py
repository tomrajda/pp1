# 15.	An array contains values: [[0,0,0],[0,0,0],[0,0,0]]. 
# Create a program that replaces the values of the main diagonal with 1. 
# Use loop statements. Display the modified array as below:
# 1 0 0
# 0 1 0
# 0 0 1

arr =  [[0,0,0],[0,0,0],[0,0,0]]

j = 0
for i in range(len(arr)):
    arr[i][j] = 1
    j += 1
    for k in arr[i]:
        print(k, end=" ")
    print()