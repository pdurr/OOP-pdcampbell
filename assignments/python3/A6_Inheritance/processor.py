# pragma once
from typing import List
from analyzer import SampleAnalyzer


class DataProcessor:
    """Class for processing multiple test cases."""

    def __init__(self) -> None:
        """Initialize DataProcessor."""
        self._cases: List[SampleAnalyzer] = []

    @property
    def cases(self) -> List[SampleAnalyzer]:
        """Getter method for the cases attribute."""
        return self._cases

    @cases.setter
    def cases(self, new_cases: List[SampleAnalyzer]) -> None:
        """Setter method for the cases attribute."""
        self._cases = new_cases

    def add_case(self, data: List[int]) -> None:
        """Add a new case with the provided data."""
        new_case = SampleAnalyzer(data)
        self.cases.append(new_case)

    def analyze_cases(self) -> None:
        """Analyze all cases and print the results."""
        for idx, case in enumerate(self.cases, start=1):
            min_val: int = case.min_value()
            max_val: int = case.max_value()
            range_val: int = case.range_value()
            print(f"Case {idx}: {min_val} {max_val} {range_val}")
