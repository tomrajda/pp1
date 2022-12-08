# 29.	Write a program that, for the given array of real numbers, displays 
# the number of elements that are greater than the given value entered from the 
# keyboard.

def greater(array, value):
    """
    
    """
    print(f"Greater numbers of array than input value:", end=" ")
    for i in array:
        if i > value:
            print(i, end=" ")

greater([1, 2, 3, 4, 5, 6, 7], 3)