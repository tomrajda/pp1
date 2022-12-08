# 36.	A two-dimensional array of size 2 by 4 contains integer numbers. 
# Create a program that displays array values in rows and columns.

def table(array):
    """
    
    """
    for i in array:
        for j in i:
            print(j, end=" ")
        print()


array = [[1,2,3], [4,5,6]]
table(array)