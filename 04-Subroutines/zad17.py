# 17.	Create a program that calculates how many times the given letter appears 
# in any text. Then create a program and check how many times the letter e’ 
# appears in the text below. Define a function for making calculations.

def calcLetter(letter, text):
    """
    Calculates how many times
    letter appears in string
    """
    counter = 0
    for i in text:
        if i == letter:
            counter += 1
    
    return counter


text = "You never get a second chance to make a first impression"

print(calcLetter("a", text))
