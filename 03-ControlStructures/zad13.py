# 13.	Write a program that calculates values for 
# the following fractions: 1/2, 1/3, ..., 1/10. 

for i in range(1, 11):
    print(f"1/{i} = {format(1 / i, '.2f')}")