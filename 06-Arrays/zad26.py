# 26.	Write a program to find the second largest element in an array. 
# Sample result:
# Array: [5,1,9,6,1]
# Result: 6

def second_largest(array):
    """
    
    """
    array.pop(array.index(max(array)))

    return max(array)

array = [5,1,9,6,1]

print(f"Array: {array}")
print(f"Result: {second_largest(array)}")