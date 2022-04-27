from collections.abc import Callable
from decorator import decorator
from typing import Any, Tuple


@decorator
def execute_twice(function: Callable, *args: Any, **kwargs: Any) -> Callable[Tuple]:
    """Returns what function return twice (inside tuple)."""
    return function(*args, **kwargs), function(*args, **kwargs)


@execute_twice
def times2(number: float) -> float:
    """Returns number * 2."""
    return number * 2


def main_execute_twice() -> None:
    """Some tests on execute_twice."""
    print(times2(7.2))


if __name__ == "__main__":
    main_execute_twice()
