"""Unit, generator, and integration tests for the FizzBuzz module."""

import io
from collections.abc import Iterator

import pytest

from fizzbuzz import evaluate_number, generate_sequence, main

EXPECTED_1_TO_100 = [
    "1",
    "2",
    "Fizz",
    "4",
    "Buzz",
    "Fizz",
    "7",
    "8",
    "Fizz",
    "Buzz",
    "11",
    "Fizz",
    "13",
    "14",
    "FizzBuzz",
    "16",
    "17",
    "Fizz",
    "19",
    "Buzz",
    "Fizz",
    "22",
    "23",
    "Fizz",
    "Buzz",
    "26",
    "Fizz",
    "28",
    "29",
    "FizzBuzz",
    "31",
    "32",
    "Fizz",
    "34",
    "Buzz",
    "Fizz",
    "37",
    "38",
    "Fizz",
    "Buzz",
    "41",
    "Fizz",
    "43",
    "44",
    "FizzBuzz",
    "46",
    "47",
    "Fizz",
    "49",
    "Buzz",
    "Fizz",
    "52",
    "53",
    "Fizz",
    "Buzz",
    "56",
    "Fizz",
    "58",
    "59",
    "FizzBuzz",
    "61",
    "62",
    "Fizz",
    "64",
    "Buzz",
    "Fizz",
    "67",
    "68",
    "Fizz",
    "Buzz",
    "71",
    "Fizz",
    "73",
    "74",
    "FizzBuzz",
    "76",
    "77",
    "Fizz",
    "79",
    "Buzz",
    "Fizz",
    "82",
    "83",
    "Fizz",
    "Buzz",
    "86",
    "Fizz",
    "88",
    "89",
    "FizzBuzz",
    "91",
    "92",
    "Fizz",
    "94",
    "Buzz",
    "Fizz",
    "97",
    "98",
    "Fizz",
    "Buzz",
]


class TestEvaluateNumber:
    """Unit tests for single-integer FizzBuzz evaluation."""

    @pytest.mark.parametrize("number", [1, 2, 4, 7, 11, 98])
    def test_returns_number_as_string(self, number: int) -> None:
        assert evaluate_number(number) == str(number)

    @pytest.mark.parametrize("number", [3, 6, 9, 12, 99])
    def test_returns_fizz_for_multiples_of_three(self, number: int) -> None:
        assert evaluate_number(number) == "Fizz"

    @pytest.mark.parametrize("number", [5, 10, 20, 25, 100])
    def test_returns_buzz_for_multiples_of_five(self, number: int) -> None:
        assert evaluate_number(number) == "Buzz"

    @pytest.mark.parametrize("number", [15, 30, 45, 60, 75, 90])
    def test_returns_fizzbuzz_for_multiples_of_three_and_five(
        self, number: int
    ) -> None:
        assert evaluate_number(number) == "FizzBuzz"

    @pytest.mark.parametrize("invalid_value", [0, -1, -15])
    def test_raises_value_error_for_non_positive(self, invalid_value: int) -> None:
        with pytest.raises(ValueError):
            evaluate_number(invalid_value)

    @pytest.mark.parametrize("invalid_type", ["3", 3.5, None, True, False])
    def test_raises_type_error_for_non_integers(self, invalid_type: object) -> None:
        with pytest.raises(TypeError):
            evaluate_number(invalid_type)  # type: ignore[arg-type]


class TestGenerateSequence:
    """Tests for the lazy 1..100 sequence generator."""

    def test_yields_100_items_lazily_with_expected_boundaries(self) -> None:
        stream = generate_sequence()
        assert isinstance(stream, Iterator)

        items = list(stream)
        assert len(items) == 100
        assert items[0] == "1"
        assert items[14] == "FizzBuzz"
        assert items[99] == "Buzz"


class TestMainIntegration:
    """End-to-end integration tests for full 1..100 output execution."""

    def test_main_writes_full_sequence_to_injected_sink(self) -> None:
        buffer = io.StringIO()
        exit_code = main(buffer)

        assert exit_code == 0
        assert buffer.getvalue().splitlines() == EXPECTED_1_TO_100

    def test_main_defaults_to_stdout(self, capsys: pytest.CaptureFixture[str]) -> None:
        exit_code = main()
        captured = capsys.readouterr()

        assert exit_code == 0
        assert captured.err == ""
        assert captured.out.splitlines() == EXPECTED_1_TO_100
