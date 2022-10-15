# Guessing game
import random

msg = "Guess the number: "

dice_roll = random.randint(1, 6)

user_num = int(input(msg))

print(dice_roll == user_num)
