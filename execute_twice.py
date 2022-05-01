from collections.abc import Callable
from decorator import decorator
from typing import Any, Tuple


@decorator
def execute_twice(function: Callable, *args: Any, **kwargs: Any) -> Callable[Tuple]:
    """
    Returns whats function returns twice (inside tuple).

    :param function: Any kind of function.
    :param args: Function arguments.
    :param kwargs: Specific arguments names and values.
    :return: A function while its return value will return twice inside a tuple.
    """
    return function(*args, **kwargs), function(*args, **kwargs)


@execute_twice
def times2(number: float) -> float:
    """
    Receives a number and return number * 2.

    :param number : A number to calculate number * 2.
    :return: The result of number * 2.
    """
    return number * 2


def main_execute_twice() -> None:
    """Some tests on execute_twice."""
    print(times2(7.2))


if __name__ == "__main__":
    main_execute_twice()
