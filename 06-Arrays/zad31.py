# 31.	Write a program to separate even and odd numbers of a given array of 
# integers. Put all even numbers first, and then odd numbers.

array = [1, 2, 3, 4, 5, 6, 7, 8, 9]
evens = []
odds = []
for i in array:
    if i % 2 == 0:
        evens.append(i)
    else:
        odds.append(i)
        
print(evens + odds)