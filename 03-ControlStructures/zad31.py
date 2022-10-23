# 32.	Write a program that displays a lottery coupon (numbers from 1 to 49) 
# in the format as below.

i = 1
for _ in range(7):
    for n in range(i, i + 43, 7):
        print(n, end=" ")
    print()
    i += 1
