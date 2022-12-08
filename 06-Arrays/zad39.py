# 39.	An array contains values: 
# [[0,0,0,0,0],0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]. 
# Create a program that modifies the array values to create a multiplication 
# table as below. Use loop statements. Display the array.
# 1  2  3  4  5
# 2  4  6  8 10
# 3  6  9 12 15
# 4  8 12 16 20
# 5 10 15 20 25

arr = [[0,0,0,0,0], [0,0,0,0,0], [0,0,0,0,0], [0,0,0,0,0], [0,0,0,0,0]]

for i in range(1, len(arr)+1):
    for j in range(i, i*(len(arr))+1, i):
        print(j, end=" ")
    print()


