from flask import Flask, jsonify
import csv

app = Flask(__name__)

airports = {}
with open("airports.csv", encoding="utf8") as file:
    reader = csv.DictReader(file)
    for row in reader:
        code = row["ident"]
        airports[code] = row

@app.route("/kentta/<icao>")
def get_airport(icao):
    icao = icao.upper()

    if icao in airports:
        airport = airports[icao]
        return jsonify({
            "ICAO": icao,
            "Name": airport["name"],
            "Municipality": airport["municipality"]
        })
    else:
        return jsonify({"error": "Airport not found"}), 404

if __name__ == "__main__":
    app.run(port=3000, debug=True)
