import unittest
from typing import List
from hypothesis import given
from hypothesis.strategies import lists, integers
from analyzer import SampleAnalyzer
from processor import DataProcessor


class TestSampleAnalyzer(unittest.TestCase):
    @given(lists(integers(), min_size=1))
    def test_min_value(self, data: List[int]) -> None:
        analyzer = SampleAnalyzer(data)
        self.assertEqual(analyzer.min_value(), min(data))

    @given(lists(integers(), min_size=1))
    def test_max_value(self, data: List[int]) -> None:
        analyzer = SampleAnalyzer(data)
        self.assertEqual(analyzer.max_value(), max(data))

    @given(lists(integers(), min_size=2))
    def test_range_value(self, data: List[int]) -> None:
        analyzer = SampleAnalyzer(data)
        self.assertEqual(analyzer.range_value(), max(data) - min(data))


class TestDataProcessor(unittest.TestCase):
    @given(lists(integers(), min_size=1))
    def test_add_case(self, data: List[int]) -> None:
        processor = DataProcessor()
        processor.add_case(data)
        self.assertEqual(len(processor.cases), 1)
        self.assertEqual(processor.cases[0].data, data)


if __name__ == "__main__":
    unittest.main()
