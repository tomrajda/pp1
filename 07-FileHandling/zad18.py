# 18.	Using any text editor, create the following two text files:

# Then write a program that creates a shoppinglist.txt file, in which save
# the contents of the MeatAndFish.txt and the GrainsAndBread.txt files.

with open("shoppinglist.txt", "w") as file:
    with open("MeatAndFish.txt", "r") as file1:
        for line in file1.readlines():
            file.writelines(line)
    file.writelines("\n")
    with open("GrainsAndBread.txt", "r") as file1:
        for line in file1.readlines():
            file.writelines(line)

