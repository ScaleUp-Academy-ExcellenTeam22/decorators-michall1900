from collections.abc import Callable
from functools import wraps
from typing import Any, Type


class InvalidTypeError(Exception):
    """
    A InvalidTypeError class, inherits from Exception.
    A custom exception that receives correct type and an object and print what the type should be.
    :ivar correct_type : The type that should be received.
    :ivar receive_arg : An argument that have been received.

    :param correct_type : The type that should be received.
    :param receive_arg : An argument that have been received.
    """
    def __init__(self, correct_type: Type[object], receive_arg: Any):
        self.correct_type = correct_type
        self.receive_arg = receive_arg

    def __str__(self):
        return f"You have been entered '{self.receive_arg}' which from type {type(self.receive_arg)}."\
               f" You should enter {self.correct_type} type"


def type_check(correct_type: Type[object]) -> Callable[Callable[Any, Any], Callable[Any, Any]]:
    """
    Returns decorator that checks if the given type is like the function's argument type.

    :param correct_type: The type that should send to function.
    :return: Decorator that will check if the type like wanted and will raise an error if it isn't.
    """
    @wraps(correct_type)
    def type_check_decorator(function: Callable[correct_type, Any]) -> Callable[correct_type, Any]:
        """
        Checking if a function that should receive one argument will receive the correct type of argument
        If the argument type isn't as wanted, InvalidTypeError will raise.
        :param function: Function that receive one argument.
        :return: Wrapper to function that check if the argument is like the correct one.
        """
        @wraps(function)
        def wrapper(argument: type(correct_type)) -> Any:
            """
            Checks if the receive type is as wanted. If it is, return what function return. Else, raise
            InvalidTypeError.

            :param argument: An argument for function.
            :return: Whats function return or raise an error.
            :raises InvalidTypeError: If the argument's type is unlike the correct one.
            """
            if not isinstance(argument, correct_type):
                raise InvalidTypeError(correct_type, argument)
            return function(argument)
        return wrapper
    return type_check_decorator


@type_check(float)
def times2(number: float) -> float:
    """Returns number * 2."""
    return number * 2


def main_type_check() -> None:
    """Tests on type check."""
    try:
        print(times2(7.4))
        print(times2("a"))
    except InvalidTypeError as error:
        print(error)


if __name__ == "__main__":
    main_type_check()
