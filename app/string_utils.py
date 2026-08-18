"""
Módulo de utilidades de cadenas y validaciones para Laboratorio 3 CI/CD.
"""
import re

def reverse_string(text: str) -> str:
    """Invierte el texto proporcionado."""
    if not isinstance(text, str):
        raise TypeError("El argumento debe ser una cadena de texto.")
    return text[::-1]

def is_palindrome(text: str) -> bool:
    """Verifica si una cadena es un palíndromo (ignorando mayúsculas y espacios)."""
    if not isinstance(text, str):
        raise TypeError("El argumento debe ser una cadena de texto.")
    cleaned = re.sub(r'[^a-zA-Z0-9]', '', text).lower()
    return cleaned == cleaned[::-1]

def validate_email(email: str) -> bool:
    """Valida el formato estándar de un correo electrónico."""
    if not isinstance(email, str):
        return False
    pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return bool(re.match(pattern, email.strip()))

def count_vowels(text: str) -> int:
    """Cuenta la cantidad de vocales (incluyendo acentuadas) en una cadena."""
    if not isinstance(text, str):
        raise TypeError("El argumento debe ser una cadena de texto.")
    vowels = "aeiouáéíóúAEIOUÁÉÍÓÚ"
    return sum(1 for char in text if char in vowels)
