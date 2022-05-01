import atexit
import math


# Global variable file to close it in the end with @atexit.register.
FILE = open("test.txt", "a")


def is_prime(num: int) -> bool:
    """Return answer to the question: is the number prime or not.
    :param num: An integer number to check if it is prime.
    :return: True if it prime, otherwise false.
    """
    # At first, checking if number is even and != 2 or < 2 (the first prime).
    # If it isn't, check if there are dividers to the received number
    # (the number should be odd or = 2).
    return False if num < 2 or (num != 2 and num % 2 == 0) \
        else all(num % div for div in range(3, math.isqrt(num) + 1, 2))


class PrimeAndPow:
    """A PrimeAndPow class for example.

    :ivar prime: An integer number.

    :param prime: An integer number.
    """
    def __init__(self, prime: int):
        """Constructor method.
        """
        self.prime = prime

    def __str__(self) -> str:
        """
        :return: String that tells what prime saved here.
        """
        return f"Prime = {self.__prime}"

    @staticmethod
    def pow(number: float, power: float) -> float:
        """Calculate number ** power. A static method for giving an example to the static
         method decorator.
        :param number: Any number to calculate its power.
        :param power: The power.
        :return: The result of number ** power.
        """
        # self._number ----> Couldn't do it
        return number ** power

    @property
    def prime(self) -> int:
        """Returns prime member. To show what is it property decorator.
        :return: Prime member.
        """
        print("At property decorator.")
        return self.__prime

    @prime.setter
    def prime(self, number: int) -> None:
        """Setter for prime number to show what is it setter decorator.
        :param number:An integer number to replace it with the current number.
                      The current number will replace with the new one only if the new one is
                      prime. Else, set the current number to 2.
        """
        print("Inside setter, checking if the value is legal.")
        try:
            if not is_prime(number):
                raise TypeError("You should enter only a prime number.")
        except (ValueError, TypeError) as error:
            print(f"{error}. Set number as 2.")
            number = 2
        finally:
            self.__prime = number


@atexit.register
def exit_message() -> None:
    """Print that at this function, closing the global file and print file.closed
     after closing file."""
    print("Bye bye from exit_message function. Using here @atexit.register. Closing file...")
    FILE.close()
    print("Answer of file.closed = ", FILE.closed)


def main_three_built_in_decorators() -> None:
    """Some tests on the decorators."""
    # We could call pow function any time without an object.
    print("Using method pow of 'Math' class without creating an object.")
    print("PrimeAndPow.pow(10, 2) = ", PrimeAndPow.pow(10, 2))
    print("-" * 80 + "\n")
    print("Trying to create math object with 3.7 as value.")
    prime_and_pow_object = PrimeAndPow(3.7)
    print(f"PrimeAndPow object str: {prime_and_pow_object}.")
    print("-" * 80 + "\n")
    print("Trying to change PrimeAndPow object value to 6.")
    prime_and_pow_object.prime = 6
    print(f"PrimeAndPow object str: {prime_and_pow_object}.")
    print("-" * 80 + "\n")
    print(f"a.number = {prime_and_pow_object.prime}.")
    print("-" * 80 + "\n")


if __name__ == "__main__":
    main_three_built_in_decorators()
    print("Program end here.")
