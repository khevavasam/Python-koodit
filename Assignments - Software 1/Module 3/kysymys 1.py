zander = float(input("Enter the length of the zander in centimeters: "))
if zander < 42:
    sudak = 42 - zander
    print("The zander does not meet the size limit.\n"
        "Please release the fish back into the lake.\n"
        "The fish was " + str(round(sudak, 2)) + " centimeters below the size limit." )

else:
    print("The zander meets the size limit.")




