"""FizzBuzz evaluation module and CLI entrypoint."""

import sys
from collections.abc import Iterator
from typing import TextIO


def evaluate_number(number: int) -> str:
    """Evaluate a single positive integer against FizzBuzz rules."""
    if isinstance(number, bool) or not isinstance(number, int):
        raise TypeError(f"Expected an integer, got {type(number).__name__}.")
    if number < 1:
        raise ValueError(f"Expected a positive integer >= 1, got {number}.")

    if number % 15 == 0:
        return "FizzBuzz"
    if number % 3 == 0:
        return "Fizz"
    if number % 5 == 0:
        return "Buzz"
    return str(number)


def generate_sequence() -> Iterator[str]:
    """Lazily yield FizzBuzz values for integers 1 through 100."""
    for number in range(1, 101):
        yield evaluate_number(number)


def main(sink: TextIO | None = None) -> int:
    """Write the 1..100 FizzBuzz sequence to the target stream."""
    output = sys.stdout if sink is None else sink
    for value in generate_sequence():
        output.write(f"{value}\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
