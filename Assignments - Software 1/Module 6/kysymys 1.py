import random
def roll_dice():
    return random.randint(1, 6)
while True:
    value = roll_dice()
    print(value)
    if value == 6:
        break
