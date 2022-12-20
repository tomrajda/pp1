# 10.	Create a program that saves, in separate lines, your name and surname, 
# university name and field of study in a text file.  Tip: open a file in 
# writing mode and then use the write() method.

data = "Tomasz Rajda\nUniwersytet Ekonomiczny\nApplied Computer Science"

file = open("my_Data.txt", 'w')

file.write(data)

file.close()