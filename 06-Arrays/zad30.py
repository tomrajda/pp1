# 30.	Create a function minmax(array) that, for the given array of integers, 
# returns a two-element array containing the smallest and largest values in 
# the given array. Sample result:
# Array:  [4,2,8,4,7,9,5]
# Result: [2,9]

def minmax(array):
    """
    
    """
    result = [min(array), max(array)]

    return result

array = [4,2,8,4,7,9,5]
print(f"Array: {array}")
print(f"Result: {minmax(array)}")