

inches = float(input("Enter length in inches (negative value to quit): "))
while inches >= 0:
    cm = inches * 2.54
    print (f"{inches} inches is {cm:.2f} centimeters")
    inches = float(input("Enter length in inches (negative value to quit): "))

print("Program ended.")