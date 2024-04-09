from weather_cli import WeatherCLI
from weather_data import WeatherData
import unittest
from unittest.mock import patch, MagicMock
import sys
import os

# Calculate the parent directory of the current script
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)

# Add the parent directory to the Python path if not already added
if parent_dir not in sys.path:
    sys.path.append(parent_dir)


class TestWeatherApp(unittest.TestCase):
    @patch("weather_data.requests.get")
    def test_get_weather(self, mock_get: MagicMock) -> None:
        mock_response = MagicMock()
        mock_response.json.return_value = {
            "location": {"name": "New York"},
            "current": {
                "condition": {"text": "Sunny"},
                "temp_f": 70,
                "humidity": 60,
                "wind_mph": 10,
                "vis_miles": 5,
            },
        }
        mock_get.return_value = mock_response

        weather_data = WeatherData()
        data = weather_data.get_weather("New York")

        self.assertIn("location", data)
        self.assertIn("current", data)

    @patch("weather_cli.Console.print")
    def test_display_weather(self, mock_print: MagicMock) -> None:
        weather_cli = WeatherCLI()
        weather_data = {
            "location": {"name": "New York"},
            "current": {
                "condition": {"text": "Sunny"},
                "temp_f": 70,
                "humidity": 60,
                "wind_mph": 10,
                "vis_miles": 5,
            },
        }
        weather_cli.display_weather("New York", weather_data)
        mock_print.assert_called()


if __name__ == "__main__":
    unittest.main()
