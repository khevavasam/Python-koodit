import requests

api_key = "7ddca5ba08b5cd05d78269dbc360c1f"
city = input("Enter municipality name: ")
url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

try:
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        description = data["weather"][0]["description"]
        temperature = data["main"]["temp"]
        print(f"Weather: {description}")
        print(f"Temperature: {temperature} Celsius")
    else:
        print("Error fetching weather data")
except requests.exceptions.RequestException as e:
    print("Network error:", e)
