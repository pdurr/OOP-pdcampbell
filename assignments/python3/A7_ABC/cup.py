# pragma once
class Cup:
    def __init__(self, color: str, radius: int) -> None:
        self._color: str = color
        self._radius: int = radius * 2 if isinstance(radius, str) else radius

    @property
    def color(self) -> str:
        return self._color

    @color.setter
    def color(self, value: str) -> None:
        self._color = value

    @property
    def radius(self) -> int:
        return self._radius

    @radius.setter
    def radius(self, value: int) -> None:
        self._radius = value * 2 if isinstance(value, str) else value

    def __lt__(self, other: 'Cup') -> bool:
        return self.radius < other.radius

    def __str__(self) -> str:
        return self._color
