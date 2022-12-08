# 35.	Define a function rand_elem(array) that returns a randomly selected 
# array element. Using the function, display a few randomly selected array
# elements.

import random

def rand_elem(array):
    """
    
    """
    
    return array[random.randint(0, len(array)-1)]



for _ in range(20):
    print(rand_elem([1,2,3,4,5]))