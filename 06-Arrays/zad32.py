# 32.	Define a function that returns the elements of the array as a string, 
# separated by commas. Using defined functions, display the contents of any array. 
# Sample result:
# Array: [5,4,3,2,6,5]
# String: 5,4,3,2,6,5

def commas(array):
    """
    
    """
    string = ""
    for i in array:
        i = str(i)
        string += i + ","
    return string[:-1]

array = [5,4,3,2,6,5]

print(f"Array: {array}")
print(f"String: {commas(array)}")