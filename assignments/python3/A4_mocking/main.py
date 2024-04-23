# pragma once
from .movie import Movie
from .cost_calculator import CostCalculator


def main() -> None:
    """Main function to handle input and output."""
    input_data = input().split()
    movie_title: str = input_data[0]
    cost_cap: float = float(input_data[1])

    movie = Movie(movie_title)
    cost_calculator = CostCalculator(movie, cost_cap)

    cost: float = cost_calculator.calculate_cost()
    print(cost)


if __name__ == "__main__":
    main()
