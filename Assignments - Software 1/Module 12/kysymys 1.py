import requests

def get_chuck_norris_joke():
    url = "https://api.chucknorris.io/jokes/random"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            print(data["value"])
        else:
            print("Error: request failed.")
    except requests.exceptions.RequestException:
        print("Network error. Please check your internet connection.")

get_chuck_norris_joke()
