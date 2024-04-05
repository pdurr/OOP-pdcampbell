from dotenv import load_dotenv
from weather_data import WeatherData
from weather_cli import WeatherCLI

load_dotenv()  # Load environment variables from .env file

if __name__ == "__main__":
    weather_data = WeatherData()
    weather_cli = WeatherCLI()

    city = input("Enter city name: ")
    data = weather_data.get_weather(city)
    weather_cli.display_weather(city, data)
