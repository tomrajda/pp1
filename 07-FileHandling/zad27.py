# 27.	The grades.txt file contains student’s grades. Create the file in any 
# text editor.
# Name: Peter
# Grades: 3.5, 4.0, 5.0, 4.5, 3.5, 3.0, 5.0
# Then create a program that calculates the arithmetic mean of student’s grades.

import re

def average(list):
    return sum(list) / len(list)

with open('grades.txt') as file:
    file_content = file.read()

    grades = [float(i) for i in re.findall('\d.\d', file_content)]

print(round(average(grades), 2))
