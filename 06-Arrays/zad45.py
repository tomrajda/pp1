# 45.	Create a function that convert two-dimensional (2D) array into 1D. 
# Then create a program that displays 1D array for the following 2D arrays.

m = [[1,2],[3,4],[5,6]]

def conv2d(m):
    """
    
    """
    m_1d = []
    for i in m:
        for j in i:
            m_1d.append(j)

    return m_1d

print(conv2d(m))