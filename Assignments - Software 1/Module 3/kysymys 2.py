command = input("Enter the cabin class (LUX, A, B, or C): ")
if command == "LUX":
    print("Upper-deck cabin with a balcony.")
elif command == "A":
    print("Above the car deck, equipped with a window.")
elif command == "B":
    print("Windowless cabin above the car deck.")
elif command == "C":
    print("Windowless cabin below the car deck.")
else:
    print("Invalid cabin class.")
