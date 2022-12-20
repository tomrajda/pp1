# 20.	Create a program that writes 50 random integers between 100 and 999 to 
# a text file, each number on a separate line.

import random

with open("rand_numbers.txt", "w") as file:
    for _ in range(50):
        file.writelines(str(random.randint(100,999))+"\n")