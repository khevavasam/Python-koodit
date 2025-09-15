import mysql.connector

def get_airports_by_country(country_code):
    conn = mysql.connector.connect(
        host="localhost",
        port=3306,
        user="root",
        password="",
        database="flight_game"
    )
    cur = conn.cursor()

    sql = """
        SELECT type, COUNT(*) 
        FROM airport 
        WHERE iso_country = %s 
        GROUP BY type
        ORDER BY type
    """
    cur.execute(sql, (country_code,))
    results = cur.fetchall()

    cur.close()
    conn.close()
    return results


def run_country_program():
    code = input("Enter the country code (e.g., FI for Finland): ").strip().upper()
    airports = get_airports_by_country(code)

    if not airports:
        print(f"No airports found for country code '{code}' or database connection failed.")
    else:
        print()
        print()
        print(f"Airports in {code}:")
        for airport_type, count in airports:
            print(f"{count} {airport_type} airports")


run_country_program()

