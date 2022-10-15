# BMI calculator

# Input data
weight = int(input("Type your weight: "))
height = int(input("Type your height: ")) / 100

# Calculations
bmi = round(weight / (height ** 2), 1)

# Data output
if bmi < 18.5:
    print(f"BMI index = {bmi} - You are underweight.")
elif bmi >= 25:
    print(f"BMI index = {bmi} - You are overweight.")
else:
    print(f"BMI index = {bmi} - You are normal.")
