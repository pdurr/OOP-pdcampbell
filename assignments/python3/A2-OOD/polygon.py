from typing import List, Tuple


class Polygon:
    """Class representing a convex polygon."""

    def __init__(self, vertices: List[Tuple[int, int]]) -> None:
        self.__vertices = vertices

    @property
    def vertices(self) -> List[Tuple[int, int]]:
        """Getter method for vertices."""
        return self.__vertices

    @vertices.setter
    def vertices(self, vertices: List[Tuple[int, int]]) -> None:
        """Setter method for vertices."""
        self.__vertices = vertices

    def calculate_area(self) -> float:
        """Calculate the area of the polygon using the shoelace formula."""
        n = len(self.__vertices)
        area = 0
        for i in range(n):
            j = (i + 1) % n
            area += (self.__vertices[i][0] * self.__vertices[j][1]) - (
                self.__vertices[j][0] * self.__vertices[i][1]
            )
        return abs(area) / 2
