# 12.	An array contains values: [[2,5,4],[9,0,3]]. 
# Create a program that displays:
# a.	the array
# b.	size of the array (number of rows and columns)
# c.	value 5 from the array
# d.	value 3 from the array
# e.	second row of the array as below:
#       9 0 3
# f.	all values from the array as below:
#       2 5 4 
#       9 0 3
# g.	last column of the array as below:
        # 4
        # 3

arr = [[2,5,4],[9,0,3]]

# a
print(arr)

# b
print(f"Rows = {len(arr)}\nColumns = {len(arr[0])}")

# c
print(arr[0][1])

# d
print(arr[-1][-1])

# e
for i in arr[1]:
    print(i, end=" ")
print()

# f
for i in arr:
    for j in i:
        print(j, end=" ")
    print()

# g
for i in arr:
    print(i[-1])
