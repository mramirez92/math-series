import pytest

from series.series import fibonacci
from series.series import lucas
from series.series import sum_series


# test fibonacci()


def test_fibonacci_3():
    actual = fibonacci(3)
    expected = 2
    assert actual == expected


def test_fibonacci_4():
    actual = fibonacci(4)
    expected = 3
    assert actual == expected


def test_fibonacci_5():
    actual = fibonacci(5)
    expected = 5
    assert actual == expected


# test lucas function


def test_lucas_3():
    actual = lucas(3)
    expected = 4
    assert actual == expected


def test_lucas_4():
    actual = lucas(4)
    expected = 7
    assert actual == expected


def test_lucas_5():
    actual = lucas(5)
    expected = 11
    assert actual == expected

# test sum_series


def test_sum_series_fibonacci3():
    actual = sum_series(3, 0, 1)
    expected = 2
    assert actual == expected


def test_sum_series_lucas3():
    actual = sum_series(3, 2, 1)
    expected = 4
    assert actual == expected



