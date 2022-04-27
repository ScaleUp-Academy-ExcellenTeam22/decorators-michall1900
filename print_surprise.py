from collections.abc import Callable
from functools import wraps


def surprise_decorator(_function: Callable) -> Callable:
    """Receives function and arguments and print surprise instead of the functionality of the function.
    :param _function: Any kind of function.
    :return: The wrapper.
    """
    @wraps(_function)
    def wrapper(*_args, **_kwargs) -> None:
        """Prints surprise."""
        print("Surprise!")
    return wrapper


@surprise_decorator
def times2(num: float) -> float:
    """Returns number * 2."""
    return num*2


def main_surprise() -> None:
    """Test surprise decorator."""
    times2(5.7)
    length = surprise_decorator(len)
    length("hello", hey=123)


if __name__ == "__main__":
    main_surprise()
