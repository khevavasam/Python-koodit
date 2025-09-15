print()
first_menu = True
airports = {}

def show_menu():
    print("Airport Data Management")
    print("1. Enter a new airport")
    print("2. Fetch airport information")
    print("3. Quit")
    print("Please choose an option (1-3): ", end="")

while True:
    if first_menu:
        first_menu = False
    show_menu()
    choice = input().strip()

    if choice == "1":
        icao = input("Enter the ICAO code: ").strip().upper()
        name = input("Enter the airport name: ").strip()
        airports[icao] = name
        print(f"Airport {name} with ICAO code {icao} has been added.\n")

    elif choice == "2":
        icao = input("Enter the ICAO code: ").strip().upper()
        if icao in airports:
            print(f"The airport with ICAO code {icao} is {airports[icao]}.\n")
        else:
            print(f"No airport found with ICAO code {icao}. \n")

    elif choice == "3":
        print("Thank you for using the Airport Data Management system. Goodbye!")
        break

    else:
        print("Invalid option. Please enter 1, 2, or 3.\n")
