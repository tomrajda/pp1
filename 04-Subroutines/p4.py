# (p4.py) Create a function f(number, even) that computes the sum of the digits 
# of a number. When the value of the even parameter is True, the function 
# returns the sum of the even digits. When the value of the even parameter is 
# False, the function returns the sum of the odd digits. Example:
# f(3124,True) => 6
# f(3124,False) => 4
# f(20576,False) => 12
# f(20576,True) => 8
# f(13115,True) => 0

def f(number, even):
    """
    Returns sum of even or odd 
    digits of input number
    """

    number = str(number)
    even_sum = 0
    odd_sum = 0

    if even:
        
        for i in number:
            i = int(i)
            if i % 2 == 0:
                even_sum += i
        
        return even_sum
    
    else:

        for i in number:
            i = int(i)
            if i % 2 != 0:
                odd_sum += i
        
        return odd_sum


print(f(3124,True)) # => 6
print(f(3124,False)) # => 4
print(f(20576,False)) # => 12
print(f(20576,True)) # => 8
print(f(13115,True)) # => 0