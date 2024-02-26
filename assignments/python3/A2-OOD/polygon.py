# polygon.py

from typing import List, Tuple


class Polygon:
    """Class representing a convex polygon."""

    def __init__(self, vertices: List[Tuple[int, int]]) -> None:
        self._vertices = vertices

    @property
    def vertices(self) -> List[Tuple[int, int]]:
        """Getter method for vertices."""
        return self._vertices

    @vertices.setter
    def vertices(self, vertices: List[Tuple[int, int]]) -> None:
        """Setter method for vertices."""
        self._vertices = vertices

    def calculate_area(self) -> float:
        """Calculate the area of the polygon using the shoelace formula."""
        n = len(self._vertices)
        area = 0
        for i in range(n):
            j = (i + 1) % n
            area += (self._vertices[i][0] * self._vertices[j][1]) - (
                self._vertices[j][0] * self._vertices[i][1]
            )
        return abs(area) / 2
