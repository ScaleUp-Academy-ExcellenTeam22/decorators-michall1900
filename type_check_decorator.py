from collections.abc import Callable
from functools import wraps
from typing import Any, Type


class InvalidTypeError(Exception):
    """An InvalidTypeError class. Inherits from Exception.
    A custom exception that receives the correct type and an object
    and prints what the type should be.

    :param correct_type : The type that should be received.
    :param receive_arg : An argument that has been received.
    """
    def __init__(self, correct_type: Type[object], receive_arg: Any):
        """Constructor method.
        """
        self.correct_type = correct_type
        self.receive_arg = receive_arg

    def __str__(self) -> str:
        """

        :return: A string that describes what is the type that should receive.
        """
        return f"You have been entered '{self.receive_arg}' which from type " \
               f"{type(self.receive_arg)}. You should enter {self.correct_type} type"


def type_check(correct_type: Type[object]) -> Callable[Callable[Any, Any], Callable[Any, Any]]:
    """Returns a decorator that checks if the given type is like the function's argument type.

    :param correct_type: The type of the parameter that should send to function.
    :return: Decorator that will check if the type like wanted and will raise an error if it isn't.
    """
    @wraps(correct_type)
    def type_check_decorator(function: Callable[correct_type, Any]) -> Callable[correct_type, Any]:
        """Check if a function that should receive one argument will receive the correct type
         of argument. If the argument type isn't as wanted, an InvalidTypeError will raise.

        :param function: A function that receives one argument.
        :return: Wrapper to function that checks if the argument has the correct type.
        """
        @wraps(function)
        def wrapper(argument: type(correct_type)) -> Any:
            """Checks if the receive type is as wanted. If it is, return what function return.
            Else, raise InvalidTypeError.

            :param argument: An argument for function.
            :return: What function return or raise an error.
            :raises InvalidTypeError: If the argument's type is unlike the correct one.
            """
            if not isinstance(argument, correct_type):
                raise InvalidTypeError(correct_type, argument)
            return function(argument)
        return wrapper
    return type_check_decorator


@type_check(float)
def times2(number: float) -> float:
    """Receives a number and return number * 2.

    :param number : A number to calculate number * 2.
    :return: The result of number * 2.
    """
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
