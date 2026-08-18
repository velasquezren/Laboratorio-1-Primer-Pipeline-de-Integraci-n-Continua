"""
Pruebas unitarias para el módulo calculator.py.
"""
import pytest
from app.calculator import (
    add,
    subtract,
    multiply,
    divide,
    power,
    factorial,
    is_even,
    calculate_discount,
)

class TestCalculatorOperations:
    def test_add_positive_numbers(self):
        assert add(10, 5) == 15

    def test_add_negative_numbers(self):
        assert add(-10, -5) == -15
        assert add(-10, 5) == -5

    def test_subtract_numbers(self):
        assert subtract(10, 4) == 6
        assert subtract(4, 10) == -6

    def test_multiply_numbers(self):
        assert multiply(6, 7) == 42
        assert multiply(-3, 5) == -15
        assert multiply(10, 0) == 0

    def test_divide_valid_numbers(self):
        assert divide(20, 4) == 5.0
        assert divide(7, 2) == 3.5

    def test_divide_by_zero_raises_exception(self):
        with pytest.raises(ZeroDivisionError, match="No es posible dividir entre cero."):
            divide(10, 0)

    def test_power_operations(self):
        assert power(2, 3) == 8
        assert power(5, 0) == 1
        assert power(2, -1) == 0.5

    def test_factorial_valid(self):
        assert factorial(0) == 1
        assert factorial(1) == 1
        assert factorial(5) == 120
        assert factorial(6) == 720

    def test_factorial_invalid_raises_value_error(self):
        with pytest.raises(ValueError, match="El factorial solo está definido para enteros no negativos."):
            factorial(-5)

    def test_is_even_cases(self):
        assert is_even(4) is True
        assert is_even(7) is False
        assert is_even(0) is True
        assert is_even(-2) is True

    def test_is_even_invalid_type_raises_error(self):
        with pytest.raises(TypeError, match="El valor debe ser un número entero."):
            is_even("4")

    def test_calculate_discount_valid(self):
        assert calculate_discount(100.0, 20.0) == 80.0
        assert calculate_discount(250.0, 0.0) == 250.0
        assert calculate_discount(150.0, 100.0) == 0.0

    def test_calculate_discount_invalid_price(self):
        with pytest.raises(ValueError, match="El precio no puede ser negativo."):
            calculate_discount(-50, 10)

    def test_calculate_discount_invalid_percentage(self):
        with pytest.raises(ValueError, match="El porcentaje de descuento debe estar entre 0 y 100."):
            calculate_discount(100, 150)
        with pytest.raises(ValueError, match="El porcentaje de descuento debe estar entre 0 y 100."):
            calculate_discount(100, -5)
