import random

dice_count = int(input("How many dice to roll: "))

total = 0
for i in range(dice_count):
    throw = random.randint(1, 6)
    total += throw

print("Sum of the dice:", total)
