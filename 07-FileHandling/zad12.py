# 12.	Create a program that allows you to add a name of next product you want 
# to buy at the end of the text file shopping.txt. Enter the product name from
#  the keyboard. Tip: open the file in appending mode.

file = open("products.txt", "a")

product = input("Enter product name: ")

file.writelines(product + "\n")

file.close()