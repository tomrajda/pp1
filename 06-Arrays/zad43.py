# 43.	Create a function identity_matrix(n) that returns an identity matrix of 
# size n (https://en.wikipedia.org/wiki/Identity_matrix). Then create a function 
# that displays a 2D array in rows and columns. Finally, create a program that 
# displays three identity matrices with dimensions of 3, 5 and 8.

def identity_m(dim):
    """
    
    """
    matrix = []
    line = []
    for i in range(0, dim):
        for j in range(0, dim):
            line.append(0)
        line[i] = 1
        matrix.append(line)
        line = []

    return matrix

print(identity_m(3))

#why i get empty places at 0 positions of matrix