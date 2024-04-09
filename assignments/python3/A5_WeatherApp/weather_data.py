import os
import requests
from typing import Dict, Any


class WeatherData:
    """Class to handle fetching weather data from an API."""

    def __init__(self) -> None:
        """Initialize WeatherData with API key and base URL."""
        self.api_key: str = os.getenv("WEATHER_API_KEY") or ""
        self.base_url: str = "https://api.weatherapi.com/v1/current.json"

    def get_weather(self, city: str) -> Dict[str, Any]:
        """
        Fetch weather data for a given city.

        Args:
            city (str): The name of the city to fetch weather data for.

        Returns:
            dict: A dictionary containing the weather data.
        """
        params: Dict[str, str] = (
            {"key": self.api_key, "q": city, "units": "imperial"})
        response: requests.Response = (
            requests.get(self.base_url, params=params))
        data: Dict[str, Any] = response.json()
        return data
