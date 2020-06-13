import pytest

from math_series.series import fibonacci, lucas, sum_series


# fibonacci tests
def test_fib_0():
    actual = fibonacci(0)
    expected = 0
    assert actual == expected


def test_fib_1():
    actual = fibonacci(1)
    expected = 1
    assert actual == expected


def test_fib_2():
    actual = fibonacci(2)
    expected = 1
    assert actual == expected


def test_fib_3():
    actual = fibonacci(3)
    expected = 2
    assert actual == expected


def test_fib_7():
    actual = fibonacci(7)
    expected = 13
    assert actual == expected


def test_fib_float():
    with pytest.raises(TypeError):
        fibonacci(7.7)


def test_fib_string():
    with pytest.raises(TypeError):
        fibonacci("7")


def test_fib_none():
    with pytest.raises(TypeError):
        fibonacci(None)


def test_fib_negative():
    with pytest.raises(IndexError):
        fibonacci(-1)


# lucas tests

def test_lucas_0():
    actual = lucas(0)
    expected = 2
    assert actual == expected


def test_lucas_1():
    actual = lucas(1)
    expected = 1
    assert actual == expected


def test_lucas_2():
    actual = lucas(2)
    expected = 3
    assert actual == expected


def test_lucas_3():
    actual = lucas(3)
    expected = 4
    assert actual == expected


def test_lucas_7():
    actual = lucas(7)
    expected = 29
    assert actual == expected


def test_lucas_float():
    with pytest.raises(TypeError):
        lucas(7.7)


def test_lucas_string():
    with pytest.raises(TypeError):
        lucas("7")


def test_lucas_none():
    with pytest.raises(TypeError):
        lucas(None)


def test_lucas_negative():
    with pytest.raises(IndexError):
        lucas(-1)


# sum series tests

def test_sum_series_0_fib():
    actual = sum_series(0)
    expected = fibonacci(0)
    assert actual == expected


def test_sum_series_1_fib():
    actual = sum_series(1)
    expected = fibonacci(1)
    assert actual == expected


def test_sum_series_2_fib():
    actual = sum_series(2)
    expected = fibonacci(2)
    assert actual == expected


def test_sum_series_3_fib():
    actual = sum_series(3)
    expected = fibonacci(3)
    assert actual == expected


def test_sum_series_7_fib():
    actual = sum_series(7)
    expected = fibonacci(7)
    assert actual == expected


def test_sum_series_0_lucas():
    actual = sum_series(0, 2, 1)
    expected = lucas(0)
    assert actual == expected


def test_sum_series_1_lucas():
    actual = sum_series(1, 2, 1)
    expected = lucas(1)
    assert actual == expected


def test_sum_series_2_lucas():
    actual = sum_series(2, 2, 1)
    expected = lucas(2)
    assert actual == expected


def test_sum_series_3_lucas():
    actual = sum_series(3, 2, 1)
    expected = lucas(3)
    assert actual == expected


def test_sum_series_7_lucas():
    actual = sum_series(7, 2, 1)
    expected = lucas(7)
    assert actual == expected


def test_sum_series_0_random():
    actual = sum_series(0, 13, 27)
    expected = 13
    assert actual == expected


def test_sum_series_1_random():
    actual = sum_series(1, 13, 27)
    expected = 27
    assert actual == expected


def test_sum_series_2_random():
    actual = sum_series(2, 13, 27)
    expected = 40
    assert actual == expected


def test_sum_series_3_random():
    actual = sum_series(3, 13, 27)
    expected = 27 + 13 + 27
    assert actual == expected


def test_sum_series_7_random():
    actual = sum_series(7, 13, 27)
    expected = 13 * 27 + 8 * 13
    assert actual == expected


def test_sum_series_float():
    with pytest.raises(TypeError):
        sum_series(7.7)


def test_sum_series_string():
    with pytest.raises(TypeError):
        sum_series("7")


def test_sum_series_none():
    with pytest.raises(TypeError):
        sum_series(None)


def test_sum_series_negative():
    with pytest.raises(IndexError):
        sum_series(-1)
