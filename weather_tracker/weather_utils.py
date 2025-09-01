import os
import requests
from dotenv import load_dotenv
from weather_module import Weather

load_dotenv()

API_KEY = os.getenv("WEATHER_API_KEY") #loaded from .env file
BASE_URL = "http://api.weatherapi.com/v1/current.json"

def fetch_weather(city):
    """
    Fetches current weather data for a given city from WeatherAPI.com.

    Args:
        city (str): The name of the city for which to fetch weather data.

    Returns:
        Weather: A Weather object containing the city's current weather information,
                 or None if an error occurs (e.g., invalid city, network issue).
    """
    if not API_KEY:
        print("Error: Weather API key not found. Please create a .env file and add your WEATHER_API_KEY.")
        return None
        
    params = {
        'key': API_KEY,
        'q': city
    }

    response = requests.get(BASE_URL, params=params)
        
    response.raise_for_status()  
        
    data = response.json()

    if 'error' in data:
            print(f"API Error for city '{city}': {data['error']['message']}")
            return None

    location_data = data['location']
    current_data = data['current']

    weather = Weather(
            city=location_data['name'],
            temperature=current_data['temp_c'],
            condition=current_data['condition']['text'],
            humidity=current_data['humidity'],
            wind_speed=current_data['wind_kph'],
            last_updated=current_data['last_updated']
        )
    return weather