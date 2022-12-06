# 10.	An array contains integer numbers. Create a program that calculates 
# and displays the number of even and odd values in the array. Use the “while” 
# loop statement.

arr = [1, 2, 3, 10, 3, 2, 3, 0, 5]

evens = 0
odds = 0
for i in arr:
    if i % 2 == 0:
        evens += 1
    else:
        odds += 1

print(f"Even numbers = {evens}\nOdd numbers = {odds}")