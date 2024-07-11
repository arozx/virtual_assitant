import requests
from geopy.geocoders import Nominatim


class WeatherUpdate:
    def __init__(self, api_key: str):
        self.api_key = api_key

    def get_lat_long(self, place):
        geolocator = Nominatim(user_agent="custom-assistant-python")
        location = geolocator.geocode({"city": place})

        print(location)
        if location:
            return location.latitude, location.longitude
        else:
            return None

    def get_weather(self, location: str) -> str:
        # Fetches the weather for the given location
        latitudes, longitudes = self.get_lat_long(location)

        response = requests.get(
            f"https://api.openweathermap.org/data/2.5/weather?lat={latitudes}&lon={longitudes}&appid={self.api_key}"
        )
        data = response.json()
        print(data)
