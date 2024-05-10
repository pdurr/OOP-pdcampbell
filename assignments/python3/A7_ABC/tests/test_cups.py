import unittest
from cup import Cup
from cup_stack import CupStack
from hypothesis import given
from hypothesis.strategies import integers, text


class TestCup(unittest.TestCase):
    @given(color=text(), radius=integers(min_value=1, max_value=1000))
    def test_cup_creation(self, color: str, radius: int) -> None:  # Added type annotations
        cup = Cup(color, radius)
        self.assertEqual(cup.color, color)
        self.assertEqual(cup.radius, radius * 2 if isinstance(radius, str) else radius)


class TestCupStack(unittest.TestCase):
    @given(colors=text(), radii=integers(min_value=1, max_value=1000))
    def test_add_cup(self, colors: str, radii: int) -> None:  # Added type annotations
        cup_stack = CupStack()
        cup = Cup(colors, radii)
        cup_stack.add_cup(cup)
        self.assertEqual(len(cup_stack.cups), 1)
        self.assertEqual(cup_stack.cups[0], cup)

    def test_sort_cups(self) -> None:  # Added return type annotation
        cup_stack = CupStack()
        cup1 = Cup('red', 10)
        cup2 = Cup('blue', 5)
        cup_stack.add_cup(cup1)
        cup_stack.add_cup(cup2)
        cup_stack.sort_cups()
        self.assertEqual(cup_stack.cups, [cup2, cup1])


if __name__ == '__main__':
    unittest.main()
