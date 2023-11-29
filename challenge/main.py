"""Main."""

from collections import defaultdict
from typing import List


class NotAnIntegerError(Exception):
    """Exception raised when an input value is not integer."""


class Stats:
    """Stats."""

    def __init__(
        self,
        max_value: int,
        less_list: List[int],
        greater_list: List[int],
        repository: defaultdict,
    ) -> None:
        self._max_value = max_value
        self._less_list = less_list
        self._greater_list = greater_list
        self._repository = repository

    def less(self, val: int) -> int:
        if val < 1:
            return 0
        elif val > self._max_value:
            return self._less_list[self._max_value + 1]
        return self._less_list[val]

    def greater(self, val: int) -> int:
        if val >= self._max_value:
            return 0
        elif val < 1:
            return self._greater_list[0]
        return self._greater_list[val]

    def between(self, left: int, right: int) -> int:
        return self.less(val=right) - self.less(val=left) + self._repository[right]


class DataCapture:
    """Data Capture."""

    def __init__(self) -> None:
        self._repository = defaultdict(int)
        self._max_value = -1

    def add(self, val: int) -> None:
        """Receive a number and add it to the repository."""
        if not isinstance(val, int):
            raise NotAnIntegerError(f"Input value {val} is not an integer.")

        self._repository[val] += 1
        self._max_value = val if val > self._max_value else self._max_value

    def build_stats(self) -> Stats:
        """Calculate stats lists and returns Stats object."""

        less_list = [0] * (self._max_value + 2)
        greater_list = [0] * (self._max_value + 2)

        for i in range(1, self._max_value + 2):
            less_list[i] = self._repository[i-1] + less_list[i-1]
            greater_list[self._max_value + 1 - i] = (
                self._repository[self._max_value + 2 - i] + greater_list[self._max_value + 2 - i]
                if i <= self._max_value else 0
            )

        greater_list[0] = greater_list[1]

        return Stats(
            max_value=self._max_value,
            less_list=less_list,
            greater_list=greater_list,
            repository=self._repository,
        )


if __name__ == "__main__":
    capture = DataCapture()
    capture.add(3)
    capture.add(9)
    capture.add(3)
    capture.add(4)
    capture.add(6)
    stats = capture.build_stats()
    print(stats.less(4))
    print(stats.greater(4))
    print(stats.between(3, 6))
