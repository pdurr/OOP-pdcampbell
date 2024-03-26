# pragma once
class Movie:
    """Represents a movie with a title."""

    def __init__(self, title: str):
        """
        Initializes a Movie object.

        Parameters:
        - title (str): The title of the movie.
        """
        self.__title = title

    @property
    def title(self) -> str:
        """Getter method to retrieve the movie title."""
        return self.__title

    @title.setter
    def title(self, new_title: str) -> None:
        """
        Setter method to update the movie title.

        Parameters:
        - new_title (str): The new title for the movie.
        """
        self.__title = new_title
