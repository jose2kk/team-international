"""Main Tests."""

import pytest

from challenge import main


def test_data_capture__add_method__ok(
    data_capture: main.DataCapture,
):
    assert data_capture._repository
    assert data_capture._max_value == 9


def test_data_capture__add_method__not_an_integer_error(
    data_capture: main.DataCapture,
):
    with pytest.raises(main.NotAnIntegerError):
        data_capture.add(3.1)


def test_data_capture__build_stats(
    data_capture: main.DataCapture,
):
    stats = data_capture.build_stats()
    assert stats._greater_list == [5, 5, 5, 3, 2, 2, 1, 1, 1, 0, 0]
    assert stats._less_list == [0, 0, 0, 0, 2, 3, 3, 4, 4, 4, 5]
    assert stats._max_value == 9


@pytest.mark.parametrize(
    "input,output",
    [
        (0, 0),
        (1, 0),
        (5, 3),
        (9, 4),
        (10, 5),
    ]
)
def test_stats__less_method(
    input: int,
    output: int,
    stats: main.Stats,
):
    assert stats.less(input) == output


@pytest.mark.parametrize(
    "input,output",
    [
        (0, 5),
        (1, 5),
        (5, 2),
        (9, 0),
        (10, 0),
    ]
)
def test_stats__greater_method(
    input: int,
    output: int,
    stats: main.Stats,
):
    assert stats.greater(input) == output


@pytest.mark.parametrize(
    "left,right,output",
    [
        (0, 1, 0),
        (0, 5, 3),
        (0, 9, 5),
        (0, 10, 5),
        (2, 5, 3),
        (2, 9, 5),
        (2, 10, 5),
        (9, 10, 1),
        (10, 11, 0),
    ]
)
def test_stats__between_method(
    left: int,
    right: int,
    output: int,
    stats: main.Stats,
):
    assert stats.between(left=left, right=right) == output
