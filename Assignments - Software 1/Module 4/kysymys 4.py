import random
number = random.randint(1, 10)
while True:
    users_number = float(input("Guess a number (1-10):"))
    if users_number < number:
        print("Too low!")
    elif users_number > number:
        print("Too high")
    else:
        print("Correct")
        break

