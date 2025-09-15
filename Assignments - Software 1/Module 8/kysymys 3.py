import mysql.connector
from geopy.distance import geodesic

def get_airport_coordinates(icao_code):
    conn = mysql.connector.connect(
        host="localhost",
        port=3306,
        user="root",
        password="",
        database="flight_game"
    )
    cur = conn.cursor()
    cur.execute("""
        SELECT latitude_deg, longitude_deg
        FROM airport
        WHERE ident = %s
    """, (icao_code,))
    row = cur.fetchone()
    cur.close()
    conn.close()

    if not row or row[0] is None or row[1] is None:
        return None
    return (float(row[0]), float(row[1]))


def run_airport_distance():
    code1 = input("Enter the ICAO code of the first airport: ").strip().upper()
    code2 = input("Enter the ICAO code of the second airport: ").strip().upper()

    coord1 = get_airport_coordinates(code1)
    coord2 = get_airport_coordinates(code2)

    if not coord1:
        print(f"Airport with ICAO code {code1} not found in the database.")
        return
    if not coord2:
        print(f"Airport with ICAO code {code2} not found in the database.")
        return
    print()
    km = geodesic(coord1, coord2).kilometers
    print()
    print(f"Distance between {code1} and {code2}: {km:.2f} kilometers")


run_airport_distance()
