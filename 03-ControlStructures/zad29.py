# 29.	Write a program that calculates the sum and arithmetic mean of numbers 
# entered from the keyboard. Entering 0 ends entering numbers. 

#Enter number: 15
#Enter number: 8
#Enter number: 10
#Enter number: 0
#RESULT: Quantity=3, Sum=33, Mean=11

nums = []
while True:
    num = int(input("Enter number: "))
    if num == 0:
        break
    else:
        nums.append(num)

print(f"RESULT: Quantity={len(nums)}, Sum={sum(nums)}, "
        f"Mean={int(sum(nums)/len(nums))}")
