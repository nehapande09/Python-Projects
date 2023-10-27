
import requests
API_KEY = 'YOUR_API_KEY'
BASE_URL = 'http://api.openweathermap.org/data/2.5/weather'

def get_weather(city_name):
    params = {
        'q': city_name,
        'appid': API_KEY,
        'units': 'metric'  # You can change this to 'imperial' for Fahrenheit
    }

    response = requests.get(BASE_URL, params=params)

    if response.status_code == 200:
        data = response.json()
        temperature = data['main']['temp']
        return temperature
    else:
        return None

if __name__ == '__main__':
    city_name = input("Enter the city name: ")
    temperature = get_weather(city_name)

    if temperature is not None:
        print(f'Temperature in {city_name}: {temperature}°C')
    else:
        print(f'Could not retrieve weather data for {city_name}. Please check the city name or your API key.')

