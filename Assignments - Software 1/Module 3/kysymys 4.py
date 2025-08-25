command = int(input("Enter a year: "))

if command % 4 == 0:
    if command % 100 == 0:
        if command % 400 == 0:
            print(str(command) + " is a leap year.")
        else:
            print(str(command) + " is not a leap year.")
    else:
        print(str(command) + " is a leap year.")
else:
    print(str(command) + " is not a leap year.")

            
