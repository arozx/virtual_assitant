import requests


class WeatherUpdate:
    def __init__(self, api_key: str):
        self.api_key = api_key

    def get_weather(self, location: str, latitudes, longitudes):
        response = requests.get(
            f"https://api.openweathermap.org/data/2.5/weather?lat={latitudes}&lon={longitudes}&appid={self.api_key}"
        )
        data = response.json()
        print(data)
