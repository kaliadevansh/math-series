import pytest

from math_series.series import fibonacci, lucas


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
