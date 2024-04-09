import unittest
from ..movie import Movie
from ..cost_calculator import CostCalculator
from hypothesis import given
from hypothesis import strategies as st


class TestMovieCostCalculator(unittest.TestCase):

    def setUp(self) -> None:
        self.movie_instance = Movie("Interstellar")
        self.cost_calculator_instance = CostCalculator(self.movie_instance, 10.5)

    def test_movie_title(self) -> None:
        self.assertEqual(self.movie_instance.title, "Interstellar")

    def test_movie_title_setter(self) -> None:
        self.movie_instance.title = "TheDarkKnight"
        self.assertEqual(self.movie_instance.title, "TheDarkKnight")

    def test_cost_calculator(self) -> None:
        self.assertEqual(
            self.cost_calculator_instance.calculate_cost(), 10.5
        )  # Minimum between len("Interstellar") and 10.5

    def test_cost_calculator_setter(self) -> None:
        self.cost_calculator_instance.cost_cap = 5.0
        self.assertEqual(
            self.cost_calculator_instance.calculate_cost(), 5
        )  # Minimum between len("Interstellar") and 5.0

    @given(
        st.text(alphabet=st.characters(min_codepoint=65, max_codepoint=122)),
        st.floats(min_value=0, max_value=100),
    )
    def test_movie_title_and_cost(self, title: str, cost_cap: float) -> None:
        movie = Movie(title)
        self.assertEqual(movie.title, title)

        cost_calculator = CostCalculator(movie, cost_cap)
        expected_cost = min(len(title), cost_cap)
        self.assertEqual(cost_calculator.calculate_cost(), expected_cost)


if __name__ == "__main__":
    unittest.main()
