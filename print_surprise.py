from collections.abc import Callable
from functools import wraps
from typing import Any


def surprise_decorator(_function: Callable) -> Callable:
    """
    Receives function and arguments and print surprise instead of the functionality of the function.

    :param _function: Any kind of function.
    :return: The wrapper.
    """
    @wraps(_function)
    def wrapper(*_args: Any, **_kwargs: Any) -> None:
        print("Surprise!")
    return wrapper


@surprise_decorator
def times2(number: float) -> float:
    """
    Receives a number and return number * 2.
    
    :param number : A number to calculate number * 2.
    :return: The result of number * 2.
    """
    return number * 2


def main_surprise() -> None:
    times2(5.7)
    length = surprise_decorator(len)
    length("hello", hey=123)


if __name__ == "__main__":
    main_surprise()
