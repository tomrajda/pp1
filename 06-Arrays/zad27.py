# 27.	Write a program that displays the difference between the largest and 
# smallest values in an array of integers. Sample result:
# Array: [5,1,9,6,1]
# Result: 8

def diff(array):

    return max(array) - min(array)

array = [5,1,9,6,1]
print(f"Array: {array}")
print(f"Result: {diff(array)}")