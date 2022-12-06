# 6.	An array contains values: 2, 3, 7, 5, 4. Create a program that 
#       displays:
# a.	the array
# b.	number of elements
# c.	first value
# d.	second value
# e.	last value
# f.	last but one value
# g.	sum of the first and last value
# h.	middle value
# i.	all array values separated by a single space (use a loop statement)
# j.	all array values from first to middle separated by a single space (use 
#       a loop statement)

arr = [2, 3, 7, 5, 4]

print(arr)
print(len(arr))
print(arr[0])
print(arr[1])
print(arr[-1])
print(arr[-2])
print(arr[0]+arr[-1])
print(len(arr)//2)

for i in arr:
    print(i, end=" ")
print()

for i in range(len(arr)//2+1):
    print(arr[i], end=" ")


