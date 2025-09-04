# def greet():
#     print("Hello!")
#     return

# print("A new day starts with a greeting.")
# greet()
# print("Now we can move to other business.")



def greet(times):
    for i in range(times):
        print("Round " + str(i+1) + " of saying hello.")
    return

print("A new day starts with greetings.")
greet(5)
print("Let's greet some more.")
greet(2)