# 44.	Create a function transpose_matrix(m) that returns transposed matrix m. 
# Then create a program that displays transposed matrices, in rows and columns, 
# for the following matrices.
# a.	1 2 3
#       4 5 6
#       7 8 9

# b.	1 2 3 4 5
#       6 7 8 9 0

# c.	5 6 7 8

def transpose_matrix(m):
    """
    
    """
    transpose_matrix = []
    line = []
    for i in range(0, len(m[0])):
        for j in range(0, len(m)):
            #i=0.j=0, i=0.j=1
            line.append(m[j][i])
        transpose_matrix.append(line)
        line =[]
    
    return transpose_matrix

print(transpose_matrix(m))

