# 24.	Write a program that calculates the number of vowels in the text:
# To be, or not to be, that is the question
# Use regular expressions and the findall() method.

import re

def countVowels(word):
    """
    
    """
    regex = re.findall('[aeiou]', word, re.IGNORECASE)

    return len(regex)

word = "To be, or not to be, that is the question"

print(countVowels(word))