# 5.	Try to create the following arrays. Then display the created array content.
# a.	arr1 = [3,7,1,0,4]
# b.	arr2 = [[2,3],[7,1],[0,4]]
# c.	arr3 = [7 for i in range(5)]
# d.	arr4 = [i for i in range(1,10)]
# e.	arr5 = [i*2 for i in range(1,10)]
# f.	arr6 = [random.randint(1,20) for i in range(10)]
# g.	arr7 = [[] for i in range(5)]
# h.	arr8 = [[1 for i in range(2)] for j in range(4)]
# i.	arr9 = [[random.randint(1,20) for i in range(3)] for j in range(5)]
# j.	an array with values: 4,0,3
# k.	50-element array filled with zeros
# l.	an array with integer values in the range of <1,30>
# m.	20-element array filled with 0 or 1 randomly
# n.	two dimensional array with five rows and two columns filled with False

import random

arr1 = [3,7,1,0,4]
arr2 = [[2,3],[7,1],[0,4]]
arr3 = [7 for i in range(5)]
arr4 = [i for i in range(1,10)]
arr5 = [i*2 for i in range(1,10)]
arr6 = [random.randint(1,20) for i in range(10)]
arr7 = [[] for i in range(5)]
arr8 = [[1 for i in range(2)] for j in range(4)]
arr9 = [[random.randint(1,20) for i in range(3)] for j in range(5)]
arr10 = [4, 0, 3]
arr11 = [0 for i in range(50)]
arr12 = [random.randint(1, 9) for i in range(1, 30)]
arr13 = [random.randint(0, 1) for i in range(20)]
arr14 = [[random.randint(1, 9) for i in range(2)] for i in range(5)]

print(arr1)
print(arr2)
print(arr3)
print(arr4)
print(arr5)
print(arr6)
print(arr7)
print(arr8)
print(arr9)
print(arr10)
print(arr11)
print(arr12)
print(arr13)
print(arr14)