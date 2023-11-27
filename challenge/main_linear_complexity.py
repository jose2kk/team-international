"""Main."""

# from collections import defaultdict


class Stats:
    """Stats."""

    def __init__(self, repository: dict) -> None:
        self._repository = repository

    def less(self, val: int) -> int:
        count = 0
        for k, v in self._repository.items():
            if k < val:
                count += v
        return count

    def greater(self, val: int) -> int:
        count = 0
        for k, v in self._repository.items():
            if k > val:
                count += v
        return count

    def between(self, left: int, right: int) -> int:
        count = 0
        for k, v in self._repository.items():
            if k >= left and k <= right:
                count += v
        return count


class DataCapture:
    """Data Capture."""

    def __init__(self) -> None:
        self._repository = dict()

    def add(self, val: int) -> None:
        try:
            self._repository[val] += 1
        except KeyError:
            self._repository[val] = 1

    def build_stats(self) -> Stats:
        return Stats(repository=self._repository)


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