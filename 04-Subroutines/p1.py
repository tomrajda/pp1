# (p1.py) The credit card number consists of 16 digits. Define a function 
# f(card_number) that masks the card number. The function returns a character 
# string in which only the first two and the last four digits of the card 
# number are visible. The remaining digits of the card number are replaced with 
# an asterisk. Example:
# f("5290312400019022") => "52**********9022"

def f(card_number):
    """
    Masks card number
    """
    part_1 = card_number[:2]
    part_2 = card_number[-4:]
    part_3 = card_number[2:][:-4]

    mask = ""
    for _ in part_3:
        mask += "*"

    return part_1 + mask + part_2

masked_card = f("5290312400019022")

if masked_card == "52**********9022":
    print(True)