# main.py

from typing import List
from polygon import Polygon


class ConvexPolygonAreaCalculator:
    """Class for calculating the area of convex polygons."""

    @staticmethod
    def read_input() -> List[Polygon]:
        """Read input from stdin."""
        polygons = []
        n = int(input())
        for _ in range(n):
            m, *coords = map(int, input().split())
            vertices = [(coords[i], coords[i + 1]) for i in range(0, len(coords), 2)]
            polygons.append(Polygon(vertices))
        return polygons

    @staticmethod
    def print_output(areas: List[float]) -> None:
        """Print the areas of polygons."""
        for area in areas:
            print(area)


def main() -> None:
    """Main function."""
    calculator = ConvexPolygonAreaCalculator()
    polygons = calculator.read_input()
    areas = [polygon.calculate_area() for polygon in polygons]
    calculator.print_output(areas)


if __name__ == "__main__":
    main()
