# 11.	Create a program that displays the name of month for a given month 
# number (1 to 12). Define a month(n) function that returns the name of month 
# for the number n. Store month names in an array. Using defined function, 
# display month names for the following month numbers: 1, 2, 11, 12.

def month(n):
    """
    Displays months
    """
    if n == 0:
        return None
    
    months = ["0", "january", "fabruary", "march",
            "april", "may", "june", "july",
            "august", "september", "october",
            "november", "december"    
            ]
    print(months[n])

month(1)
month(2)
month(11)
month(12)
