import unittest
from unittest.mock import patch
from io import StringIO
from main import ConvexPolygonAreaCalculator
from polygon import Polygon  # Import Polygon class
from typing import List, Any  # Import Any


class TestConvexPolygonAreaCalculator(unittest.TestCase):
    """Test cases for ConvexPolygonAreaCalculator class."""

    @patch('builtins.input', side_effect=['2', '3 1 1 2 1 2 2', '4 0 0 10 0 13 5 10 8'])
    def test_read_input(self, mock_input: Any) -> None:
        """Test read_input method."""
        calculator: ConvexPolygonAreaCalculator = ConvexPolygonAreaCalculator()
        polygons: List[Polygon] = calculator.read_input()
        self.assertEqual(len(polygons), 2)

    @patch('sys.stdout', new_callable=StringIO)
    def test_print_output(self, mock_stdout: Any) -> None:
        """Test print_output method."""
        calculator: ConvexPolygonAreaCalculator = ConvexPolygonAreaCalculator()
        calculator.print_output([0.5, 52])
        self.assertEqual(mock_stdout.getvalue(), "0.5\n52\n")


if __name__ == "__main__":
    unittest.main()
