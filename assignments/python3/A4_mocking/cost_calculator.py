# pragma once
from .movie import Movie


class CostCalculator:
    """Calculates the cost of transmitting a movie title."""

    def __init__(self, movie: Movie, cost_cap: float):
        """
        Initializes a CostCalculator object.

        Parameters:
        - movie (Movie): The movie object.
        - cost_cap (float): The cap on the cost.
        """
        self.__movie = movie
        self.__cost_cap = cost_cap

    @property
    def movie(self) -> Movie:
        """Getter method to retrieve the movie object."""
        return self.__movie

    @movie.setter
    def movie(self, new_movie: Movie) -> None:
        """
        Setter method to update the movie object.

        Parameters:
        - new_movie (Movie): The new movie object.
        """
        self.__movie = new_movie

    @property
    def cost_cap(self) -> float:
        """Getter method to retrieve the cost cap."""
        return self.__cost_cap

    @cost_cap.setter
    def cost_cap(self, new_cost_cap: float) -> None:
        """
        Setter method to update the cost cap.

        Parameters:
        - new_cost_cap (float): The new cost cap.
        """
        self.__cost_cap = new_cost_cap

    def calculate_cost(self) -> float:
        """
        Calculates the cost of transmitting the movie title.

        Returns:
        - float: The calculated cost.
        """
        return min(len(self.__movie.title), self.__cost_cap)
