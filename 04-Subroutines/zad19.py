# 19.	Define a function that checks if the number is within the given range 
# <x, y>. The function returns boolean value. 
# Then create a program and use the function you defined.

def inRange(number, x, y):
    """
    Checks if the number is
    in the entered range
    """
    if number >= x and number <= y:
        return True
    else:
        return False

print(inRange(3, 0, 5))
print(inRange(6, 0, 5))