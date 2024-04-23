from rich.console import Console
from rich.table import Table
from typing import Dict, Any


class WeatherCLI:
    """Class to display weather information in a formatted table."""

    def __init__(self) -> None:
        """Initialize WeatherCLI with a console."""
        self.__console: Console = Console()

    @property
    def console(self) -> Console:
        """Getter method for the console attribute."""
        return self.__console

    @console.setter
    def console(self, new_console: Console) -> None:
        """Setter method for the console attribute."""
        self.__console = new_console

    def display_weather(self, city: str, weather_data: Dict[str, Any]) -> None:
        """
        Display weather information for a city.

        Args:
            city (str): The name of the city.
            weather_data (dict): A dictionary containing the weather data.
        """
        if "error" in weather_data:
            self.console.print("[bold red]Error:[/bold red] City not found.")
        else:
            weather_description: str = (
                weather_data["current"]["condition"]["text"])
            temperature: float = weather_data["current"]["temp_f"]
            humidity: int = weather_data["current"]["humidity"]
            wind_speed: float = weather_data["current"]["wind_mph"]
            visibility: float = weather_data["current"]["vis_miles"]
            city_name: str = weather_data["location"]["name"]

            table: Table = Table(show_header=True, header_style="bold magenta")
            table.add_column("City", style="cyan", header_style="bold magenta")
            table.add_column("Weather", style="yellow",
                             header_style="bold magenta")
            table.add_column(
                "Temperature (°F)", style="green", header_style="bold magenta"
            )
            table.add_column("Humidity (%)", style="blue",
                             header_style="bold magenta")
            table.add_column(
                "Wind Speed (mph)",
                style="magenta", header_style="bold magenta"
            )
            table.add_column(
                "Visibility (miles)", style="cyan", header_style="bold magenta"
            )

            table.add_row(
                city_name,
                weather_description,
                f"{temperature}°F",
                f"{humidity}%",
                f"{wind_speed} mph",
                f"{visibility} miles",
            )

            self.console.print(table)
