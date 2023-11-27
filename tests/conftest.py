"""Conftest."""

import pytest

from challenge import main


@pytest.fixture
def data_capture() -> main.DataCapture:
    dc = main.DataCapture()
    dc.add(3)
    dc.add(9)
    dc.add(3)
    dc.add(4)
    dc.add(6)
    return dc


@pytest.fixture
def stats(
    data_capture: main.DataCapture,
) -> main.Stats:
    return data_capture.build_stats()
