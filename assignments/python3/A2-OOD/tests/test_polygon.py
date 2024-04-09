import unittest
from polygon import Polygon
from typing import List, Tuple


class TestPolygon(unittest.TestCase):
    """Test cases for Polygon class."""

    def test_calculate_area(self) -> None:
        """Test calculate_area method."""
        # Test case with a triangle
        vertices_triangle: List[Tuple[int, int]] = [(0, 0), (0, 2), (3, 0)]
        polygon_triangle: Polygon = Polygon(vertices_triangle)
        self.assertEqual(polygon_triangle.calculate_area(), 3.0)

        # Test case with a quadrilateral
        vertices_quadrilateral: List[Tuple[int, int]] = [(0, 0), (0, 4), (4, 4), (4, 0)]
        polygon_quadrilateral: Polygon = Polygon(vertices_quadrilateral)
        self.assertEqual(polygon_quadrilateral.calculate_area(), 16.0)


if __name__ == "__main__":
    unittest.main()
