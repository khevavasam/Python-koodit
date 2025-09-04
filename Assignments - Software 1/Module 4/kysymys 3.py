
numbers = []
users_number = input("Enter a number (or press Enter to quit): ")
while users_number != "":
    number = float(users_number)
    numbers.append(number)
    users_number = input("Enter a number (or press Enter to quit): ")

if numbers:
    print("Smallest number:", min(numbers))
    print("Largest number:", max(numbers))
