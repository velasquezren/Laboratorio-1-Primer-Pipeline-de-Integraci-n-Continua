"""
Punto de entrada principal de la aplicación.
"""
from app.calculator import add, multiply, calculate_discount
from app.string_utils import validate_email, is_palindrome

def main():
    print("=========================================")
    print("  CI/CD App - Módulo de Pruebas Unitarias")
    print("=========================================")
    print(f"Suma 15 + 25 = {add(15, 25)}")
    print(f"Multiplicación 6 * 7 = {multiply(6, 7)}")
    print(f"Descuento $100 con 15% = ${calculate_discount(100, 15)}")
    print(f"Es 'reconocer' palíndromo? -> {is_palindrome('reconocer')}")
    print(f"Validar correo 'devops@uagrm.edu.bo' -> {validate_email('devops@uagrm.edu.bo')}")
    print("=========================================")

if __name__ == "__main__":
    main()
