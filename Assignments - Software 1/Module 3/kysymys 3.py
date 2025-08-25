command = input("Enter biological gender (male/female): ").lower()
command2 = float(input("Enter hemoglobin value (g/l): "))

if command == "male":
    if 134 <= command2 <= 167:
        print("Your hemoglobin is normal.")
    elif command2 > 167:
        print("Your hemoglobin is high.")
    elif command2 < 134:
        print("Your hemoglobin is low.")
elif command == "female":
    if 117 <= command2 <= 155:
        print("Your hemoglobin is normal.")
    elif command2 > 155:
        print("Your hemoglobin is high.")
    elif command2 < 117:
        print("Your hemoglobin is low.")
else:
    print("Invalid gender.")
