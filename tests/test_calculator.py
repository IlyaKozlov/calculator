import pytest

from calculator import Calculator


@pytest.fixture()
def calculator():
    return Calculator()


def test_add_returns_sum(calculator):
    assert calculator.add(2, 3) == 5


def test_add_handles_negative_and_float_values(calculator):
    assert calculator.add(-2.5, 4.0) == pytest.approx(1.5)


def test_subtract_returns_difference(calculator):
    assert calculator.subtract(10, 4) == 6


def test_multiply_returns_product(calculator):
    assert calculator.multiply(6, 7) == 42


def test_divide_returns_quotient(calculator):
    assert calculator.divide(9, 3) == 3


def test_divide_handles_fractional_result(calculator):
    assert calculator.divide(7, 2) == pytest.approx(3.5)


def test_divide_raises_value_error_when_dividing_by_zero(calculator):
    with pytest.raises(ValueError, match="Second number cannot be zero"):
        calculator.divide(5, 0)
