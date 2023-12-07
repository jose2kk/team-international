"""Main Tests."""

from typing import Union

import pytest

from challenge import main


def test_data_capture__add_method__ok(
    data_capture: main.DataCapture,
):
    assert data_capture._repository
    assert data_capture._max_value == 9


@pytest.mark.parametrize(
    "input,error",
    [
        (3.1, main.NotAnIntegerError),
        (-1, main.InputOutOfRangeError),
        (1001, main.InputOutOfRangeError),
    ]
)
def test_data_capture__add_method__errors(
    input: Union[int, float],
    error: Exception,
    data_capture: main.DataCapture,
):
    with pytest.raises(error):
        data_capture.add(input)


def test_data_capture__build_stats(
    data_capture: main.DataCapture,
):
    stats = data_capture.build_stats()
    assert stats._greater_list == [5, 5, 3, 2, 2, 1, 1, 1, 0, 0]
    assert stats._less_list == [0, 0, 0, 0, 2, 3, 3, 4, 4, 4, 5]
    assert stats._max_value == 9


@pytest.mark.parametrize(
    "input,output",
    [
        (1, 0),
        (5, 3),
        (9, 4),
        (10, 5),
    ]
)
def test_stats__less_method__ok(
    input: int,
    output: int,
    stats: main.Stats,
):
    assert stats.less(input) == output


@pytest.mark.parametrize(
    "input",
    [-1, 1001],
)
def test_stats__less_method__input_out_of_range_error(
    input: int,
    stats: main.Stats,
):
    with pytest.raises(main.InputOutOfRangeError):
        assert stats.less(input)


@pytest.mark.parametrize(
    "input,output",
    [
        (1, 5),
        (5, 2),
        (9, 0),
        (10, 0),
    ]
)
def test_stats__greater_method__ok(
    input: int,
    output: int,
    stats: main.Stats,
):
    assert stats.greater(input) == output


@pytest.mark.parametrize(
    "input",
    [-1, 1001],
)
def test_stats__greater_method__input_out_of_range_error(
    input: int,
    stats: main.Stats,
):
    with pytest.raises(main.InputOutOfRangeError):
        assert stats.greater(input)


@pytest.mark.parametrize(
    "left,right,output",
    [
        (1, 1, 0),
        (1, 5, 3),
        (1, 9, 5),
        (1, 10, 5),
        (2, 5, 3),
        (2, 9, 5),
        (2, 10, 5),
        (9, 10, 1),
        (10, 11, 0),
        (5, 1, 0),
    ]
)
def test_stats__between_method__ok(
    left: int,
    right: int,
    output: int,
    stats: main.Stats,
):
    assert stats.between(left=left, right=right) == output


@pytest.mark.parametrize(
    "left,right",
    [
        (-1, 100),
        (100, 10001),
        (-1, 1001),
    ],
)
def test_stats__between_method__errors(
    left: int,
    right: int,
    stats: main.Stats,
):
    with pytest.raises(main.InputOutOfRangeError):
        assert stats.between(left=left, right=right)
