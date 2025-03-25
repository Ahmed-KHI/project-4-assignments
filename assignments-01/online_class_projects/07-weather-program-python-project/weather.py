import requests

API_KEY = '1afafe59d9fd1da6746ebe9bede3f00b'  
BASE_URL = 'https://api.openweathermap.org/data/2.5/weather'

def get_weather(city):
    url = f"{BASE_URL}?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)

    try:
        data = response.json()
        if data.get("cod") == 200:
            city_name = data["name"]
            temperature = data["main"]["temp"]
            description = data["weather"][0]["description"]
            print(f"Weather in {city_name}:")
            print(f"Temperature: {temperature}°C")
            print(f"Condition: {description.capitalize()}")
        else:
            print(f"Error: {data.get('message', 'City not found')}")
    except Exception as e:
        print(f"Failed to retrieve weather data: {e}")

# Input from user
city = input("Enter city name: ")
get_weather(city)