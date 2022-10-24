# 6.	Define a function that displays numbers in the layout as below 
# (like on a phone keypad). Apply an loop statement. Then call the function.
#1 2 3
#4 5 6
#7 8 9

def displayNums():
    """
    Displays numbers like
    on a phone keypad
    """
    n = 3
    for _ in range(3):
        for i in range(n-2, n+1):
            print(i, end=" ")
        print()
        n += 3

displayNums()