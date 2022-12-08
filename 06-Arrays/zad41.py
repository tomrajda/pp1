# 41.	A two-dimensional array of the size 3 by 5 contains integer numbers. 
# Create a program that swaps the first and the last row. Display array values 
# in rows and columns before and after changes.

arr = [[1,2,3],[4,5,6],[7,8,9]]

print("Before:")
for i in arr:
    for j in i:
        print(j, end=" ")
    print()

print("After:")
for i in range(0, len(arr), 2):
    for j in arr[i]:
        print(j, end=" ")
    print()