# 25.	Write a program that computes the number of words in the following text. 
# Use regular expressions.
# To be, or not to be, that is the question

import re

def countWords(txt):
    """
    
    """
    regex = re.findall('\w+', txt, re.IGNORECASE)

    return len(regex)

txt = "To be, or not to be, that is the question"

print(countWords(txt))