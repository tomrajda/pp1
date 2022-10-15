# Calculation of triangle area (by Heron formula)
import math
# Input data

a = int(input("Type a side: "))
b = int(input("Type b side: "))
c = int(input("Type c side: "))

# Calculations
s = (a+b+c) / 2
area = math.sqrt((s * (s-a) * (s-b) * (s-c)))

# Output data
print(f"Area: {area}")
