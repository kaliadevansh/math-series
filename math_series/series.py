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


def sum_series(element_index, first_element=0, second_element=1):
    """
    This function returns the nth element of a sum series. The function is built using recursion.
    The first two elements of the series are expected as inputs (or the series acts as fibonacci). The function
    calculates the n-th number of the series.
    :param element_index: index of element to be calculated.
    :param first_element: first element of the sum series. Optional - defaults to 0.
    :param second_element: second element of the sum series. Optional - defaults to 1.
    :return: n-th number of the sum-series.
    """
    if not isinstance(element_index, int):
        raise TypeError()
    elif element_index < 0:
        raise IndexError()
    elif element_index == 0:
        return first_element
    elif element_index == 1:
        return second_element
    elif element_index > 1:
        return sum_series(element_index - 1, first_element, second_element) + sum_series(element_index - 2,
                                                                                         first_element,
                                                                                         second_element)
