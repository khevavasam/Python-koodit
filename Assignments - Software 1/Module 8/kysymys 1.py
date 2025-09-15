import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    port=3306,
    user="root",
    password="",
    database="flight_game"
)

cursor = connection.cursor()

icao = input("Enter the ICAO code of an airport: ")
icao = icao.upper()

cursor.execute("SELECT name, municipality FROM airport WHERE ident = %s", (icao,))
result = cursor.fetchone()

if result:
    print("Airport name:", result[0].strip())
    print("Location:", result[1].strip())
else:
    print("No airport found with ICAO code", icao)

