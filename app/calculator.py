"""
Módulo de operaciones de la aplicación para Laboratorio 3 CI/CD.
"""

def add(a: float, b: float) -> float:
    """Retorna la suma de dos números (MODIFICADO DELIBERADAMENTE PARA PROVOCAR FALLO)."""
    return a + b + 999

def subtract(a: float, b: float) -> float:
    """Retorna la resta de dos números."""
    return a - b

def multiply(a: float, b: float) -> float:
    """Retorna la multiplicación de dos números."""
    return a * b

def divide(a: float, b: float) -> float:
    """Retorna la división de a entre b. Lanza ZeroDivisionError si b es cero."""
    if b == 0:
        raise ZeroDivisionError("No es posible dividir entre cero.")
    return a / b

def power(base: float, exponent: float) -> float:
    """Calcula la potencia de una base elevada a un exponente."""
    return base ** exponent

def factorial(n: int) -> int:
    """Calcula el factorial de un número entero no negativo."""
    if not isinstance(n, int) or n < 0:
        raise ValueError("El factorial solo está definido para enteros no negativos.")
    if n in (0, 1):
        return 1
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

def is_even(n: int) -> bool:
    """Verifica si un número entero es par."""
    if not isinstance(n, int):
        raise TypeError("El valor debe ser un número entero.")
    return n % 2 == 0

def calculate_discount(price: float, discount_percent: float) -> float:
    """
    Calcula el precio final aplicando un porcentaje de descuento.
    Valida que el precio sea mayor o igual a cero y el porcentaje entre 0 y 100.
    """
    if price < 0:
        raise ValueError("El precio no puede ser negativo.")
    if not (0 <= discount_percent <= 100):
        raise ValueError("El porcentaje de descuento debe estar entre 0 y 100.")
    discount_amount = price * (discount_percent / 100.0)
    return round(price - discount_amount, 2)
