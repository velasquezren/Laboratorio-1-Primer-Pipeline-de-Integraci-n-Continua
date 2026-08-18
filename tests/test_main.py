"""
Pruebas unitarias para el punto de entrada main.py.
"""
import runpy
from app.main import main

def test_main_execution(capsys):
    main()
    captured = capsys.readouterr()
    assert "CI/CD App - Módulo de Pruebas Unitarias" in captured.out
    assert "Suma 15 + 25 = 40" in captured.out
    assert "Multiplicación 6 * 7 = 42" in captured.out
    assert "Descuento $100 con 15% = $85.0" in captured.out
    assert "Es 'reconocer' palíndromo? -> True" in captured.out
    assert "Validar correo 'devops@uagrm.edu.bo' -> True" in captured.out

def test_main_as_script(capsys):
    runpy.run_module('app.main', run_name='__main__')
    captured = capsys.readouterr()
    assert "CI/CD App - Módulo de Pruebas Unitarias" in captured.out
