import requests
import sys

# You need to get an API key from OpenWeatherMap (or another weather API provider)
# Sign up at: https://openweathermap.org/api
API_KEY = "YOUR_OPENWEATHERMAP_API_KEY"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

def get_weather(city):
    if API_KEY == "YOUR_OPENWEATHERMAP_API_KEY":
        print("Please replace 'YOUR_OPENWEATHERMAP_API_KEY' with your actual OpenWeatherMap API key.")
        return

    params = {
        'q': city,
        'appid': API_KEY,
        'units': 'metric' # or 'imperial' for Fahrenheit
    }

    try:
        response = requests.get(BASE_URL, params=params)
        data = response.json()

        if data['cod'] == 200:
            main_data = data['main']
            weather_data = data['weather'][0]

            print(f"\nWeather in {city}:")
            print(f"Temperature: {main_data['temp']}°C")
            print(f"Feels like: {main_data['feels_like']}°C")
            print(f"Condition: {weather_data['description'].capitalize()}")
            print(f"Humidity: {main_data['humidity']}% ")
            print(f"Pressure: {main_data['pressure']} hPa")
            print(f"Wind Speed: {data['wind']['speed']} m/s")
        else:
            print(f"Error: {data['message']}")

    except requests.exceptions.RequestException as e:
        print(f"Error connecting to weather service: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    print("--- Simple Weather App ---")
    if len(sys.argv) != 2:
        print("Usage: python weather_app.py <CITY_NAME>")
        print("Example: python weather_app.py London")
    else:
        city_name = sys.argv[1]
        get_weather(city_name)
