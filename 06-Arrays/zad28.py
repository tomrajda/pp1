# 28.	Define a median(array) function that returns the median of the 
# given array of numbers. Do not use built-in functions. The median is the 
# middle value in the ordered sequence of numbers 
# (https://en.wikipedia.org/wiki/Median#/media/File:Finding_the_median.png). 
# Then, using the defined function, calculate and display the median for the 
# following values:
# a.	[1,0,9,4,6]
# b.	[6,8,3,1,0,5,7]

def median(array):
    """
    
    """

    return sorted(array)[len(array)//2]

print(median([1,0,9,4,6]))
print(median([6,8,3,1,0,5,7]))