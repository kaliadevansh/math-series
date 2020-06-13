"""
This module offers functions for mathematical series - fibonacci.
"""


def fibonacci(n):
    """
    This function returns the nth fibonacci number. The function is built using recursion.
    :param n: Index of number of fibonacci series to be returned. The series starts at 0.
    :return: n-th number from the fibonacci series.
    """
    if not isinstance(n, int):
        raise TypeError()
    elif n < 0:
        raise IndexError()
    elif n > 1:
        return fibonacci(n - 1) + fibonacci(n - 2)
    return n


def lucas(n):
    """
    This function returns the nth lucas number. The function is built using recursion.
    :param n: Index of number of lucas series to be returned. The series starts at 0.
    :return: n-th number from the lucas series.
    """
    if not isinstance(n, int):
        raise TypeError()
    elif n < 0:
        raise IndexError()
    elif n > 1:
        return lucas(n - 1) + lucas(n - 2)
    return 2 - n
