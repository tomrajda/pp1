# 34.	Write a program that checks whether the first array is a subset of the 
# second one (whether all elements of the first array appear in the second array).

def check(arr1, arr2):
    """
    
    """
    for i in arr1:
        if i not in arr2:
            return False
    return True

arr2 = [1, 2, 3, 4, 5]
arr1 = [1, 2, 3, 6]
if check(arr1, arr2):
    print(f"Yes, {arr1} is subset of {arr2}")
else:
    print(f"No, {arr1} isnt subset of {arr2}")