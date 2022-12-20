# 13.	The following program displays the contents of a file, line by line:
# f = open("filename.txt")
# for line in f:
#     print(line, end="")
# f.close()
# Rewrite the program using the "with ..." as construct. 
# Then check that the program is working properly.

with open("countries.txt", "r") as file:
    print(file.read())

