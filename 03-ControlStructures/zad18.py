# 18.	There are coins of 1, 2 and 5 Polish Zlotys (PLN). 
# Write a program showing any amount (natural number) 
# read from the keyboard with as few coins as possible.

msg1 = "Enter the amount in PLN: "
value = int(input(msg1))

msg2 = f"The amount of PLN {value} in coins:"
print(msg2)

# Checking how many 5-bilons are
bilon = 5
if value >= bilon:
    fives = int(value / bilon)
    print(f"5 zł - {fives}")
    value = value - (fives * bilon)
else:
    print(f"5 zł - 0")

# Checking how many 2-bilons are
bilon = 2
if value >= bilon:
    twos = int(value / bilon)
    print(f"2 zł - {twos}")
    value = value - (twos * bilon)
else:
    print(f"2 zł - 0")    

# Checking how many 1-bilons are
bilon = 1
if value >= bilon:
    ones = int(value / bilon)
    print(f"1 zł - {ones}")
else:
    print(f"1 zł - 0") 