"""
Pruebas unitarias para el módulo string_utils.py.
"""
import pytest
from app.string_utils import reverse_string, is_palindrome, validate_email, count_vowels

class TestStringUtilsOperations:
    def test_reverse_string_valid(self):
        assert reverse_string("DevOps") == "spOveD"
        assert reverse_string("") == ""
        assert reverse_string("12345") == "54321"

    def test_reverse_string_invalid_type(self):
        with pytest.raises(TypeError, match="El argumento debe ser una cadena de texto."):
            reverse_string(12345)

    def test_is_palindrome_valid(self):
        assert is_palindrome("reconocer") is True
        assert is_palindrome("Anita lava la tina") is True
        assert is_palindrome("A Santa at NASA") is True
        assert is_palindrome("Hola Mundo") is False

    def test_is_palindrome_invalid_type(self):
        with pytest.raises(TypeError, match="El argumento debe ser una cadena de texto."):
            is_palindrome(None)

    def test_validate_email_valid(self):
        assert validate_email("rene.velasquez@ficct.uagrm.edu.bo") is True
        assert validate_email("usuario.test@gmail.com") is True
        assert validate_email("admin@empresa.org") is True

    def test_validate_email_invalid(self):
        assert validate_email("correo_invalido.com") is False
        assert validate_email("usuario@") is False
        assert validate_email("@dominio.com") is False
        assert validate_email("") is False
        assert validate_email(12345) is False

    def test_count_vowels_valid(self):
        assert count_vowels("Integracion Continua") == 9
        assert count_vowels("rhythm") == 0
        assert count_vowels("murciélago") == 5

    def test_count_vowels_invalid_type(self):
        with pytest.raises(TypeError, match="El argumento debe ser una cadena de texto."):
            count_vowels(123)
