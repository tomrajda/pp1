# 16.	Find any text file on the Internet and download it to your computer. 
# Then write a program that copies the contents of this file to the copy.txt 
# file. Copy the contents of the file as a whole. Finally, open both files in 
# any text editor and check that their contents are the same.

with open("sample3.txt") as file:
    with open ("copy_sample3.txt", "w") as copy_file:
        for line in file:
            copy_file.write(line)
