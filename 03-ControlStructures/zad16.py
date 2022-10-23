# 16.	Write a program that displays two numbers entered 
# from the keyboard in ascending order.

msg = "first"
nums = []
for _ in range(2):
    num = int(input(f"Enter {msg} number: "))
    msg = "second"
    nums.append(num)

msg = f"Numbers in asceding order: {min(nums)}, {max(nums)}"
print(msg)