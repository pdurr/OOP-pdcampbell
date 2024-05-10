# pragma once
from cup import Cup


class CupStack:
    def __init__(self) -> None:
        self._cups: list[Cup] = []

    @property
    def cups(self) -> list[Cup]:
        return self._cups

    def add_cup(self, cup: Cup) -> None:
        self._cups.append(cup)

    def sort_cups(self) -> None:
        self._cups.sort()

    def print_sorted_colors(self) -> None:
        for cup in self._cups:
            print(cup)

    def read_input(self) -> None:
        n: int = int(input())
        for _ in range(n):
            info: list[str] = input().split()
            if info[0].isdigit():
                diameter: int = int(info[0])
                color: str = info[1]
                self.add_cup(Cup(color, diameter // 2))
            else:
                cup_color: str = info[0]
                radius: int = int(info[1])
                self.add_cup(Cup(cup_color, radius))

    def solve(self) -> None:
        self.read_input()
        self.sort_cups()
        self.print_sorted_colors()
