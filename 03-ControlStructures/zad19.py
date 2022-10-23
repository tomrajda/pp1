# 19.	Write a program that calculates a dog's age in dog’s years. 
# For the first two years, a dog's life is equal to 10.5 human years. 
# After that, each dog year is equal to 4 human years.

msg1 = "Enter the dog's age in human years: "
dog = int(input(msg1))

if dog <= 2:
    age = dog * 10.5
    print(f"The dog's age in dog’s years is {float(age)} years.")
else:
    age = (2 * 10.5) + (dog - 2) * 4
    print(f"The dog's age in dog’s years is {float(age)} years.")
