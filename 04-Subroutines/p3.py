# (p3.py) The vending machine accepts 1, 2 and 5 PLN coins. Define the function 
# f(amount_to_pay) that returns the minimum number of coins that can be used to 
# pay for the purchased product. Example:
# f(23) => 6
# f(8) => 3
# f(2) => 1
# f(0) => 0

def f(amount_to_pay):
    """
    Retruns minimum number
    of coins that can be used
    to pay for purchased product
    """
    a = int(amount_to_pay)

    bilons = 0

    if a >= 5:
        fives = int(a / 5)
        a = a - (fives * 5)
        bilons += fives
    if a >= 2:
        twos = int(a / 2)
        a = a - (twos * 2)
        bilons += twos
    if a >= 1:
        bilons += 1

    return bilons