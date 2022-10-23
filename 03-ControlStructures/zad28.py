# 28.	Write a program that displays the first fifty words of the Fibonacci 
# sequence. The sequence is defined as follows: the first term is equal to 0, 
# the second is equal to 1, each subsequent term is the sum of the previous two.
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144.

print(0, end=" ")
i = 0
j = 1
for _ in range(51):
    k = i + j
    print(j, end=" ")
    
    j = k
    i = k - i
