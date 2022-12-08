# 24.	Create a program that displays all unique elements in an array. 
# Sample result:
# Array: 2 3 2 5 8 1 9 8
# Unique elements: 3 5 1 9

arr = [2, 3, 2, 5, 8, 1, 9, 8]

print("Array:", end=" ")
for i in arr:
    print(i, end=" ")

print()

print("Unique array:", end=" ")
for i in arr:
    counter = 0
    for k in arr:
        if i == k:
            counter += 1
    if counter < 2:
        print(i, end=" ")

