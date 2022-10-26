# (p2.py) The binary system uses two symbols to represent a number: 0 and 1. 
# Define a function f(binary_number) that returns True if the given notation 
# is a valid binary number, or false otherwise. Example:
# f("101101") => True
# f("1311a10100") => False

def f(binary_number):

    """
    Checks if the given notation
    is a valid binary number
    """

    for i in binary_number:
        if i == "1" or i == "0":
            continue
        else:
            return False
    return True

print(f("1311a10100"))
