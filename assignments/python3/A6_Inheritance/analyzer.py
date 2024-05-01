# pragma once
from typing import List


class SampleAnalyzer:
    """Class for analyzing samples of data."""

    def __init__(self, data: List[int]) -> None:
        """Initialize SampleAnalyzer with data."""
        self._data: List[int] = data

    @property
    def data(self) -> List[int]:
        """Getter method for the data attribute."""
        return self._data

    @data.setter
    def data(self, new_data: List[int]) -> None:
        """Setter method for the data attribute."""
        self._data = new_data

    def min_value(self) -> int:
        """Compute and return the minimum value in the data."""
        return min(self.data)

    def max_value(self) -> int:
        """Compute and return the maximum value in the data."""
        return max(self.data)

    def range_value(self) -> int:
        """Compute and return the range of values in the data."""
        return self.max_value() - self.min_value()
