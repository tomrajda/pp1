# Random dice roll x 3
import random

# Calculations
roll_sum = 0
for _ in range(3):
    roll_sum += random.randint(1, 6)

# Data output
print(roll_sum)