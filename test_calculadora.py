# test_calculadora.py

from calculadora import sumar  # Asegúrate de que la función sumar esté en calculadora.py

def test_suma_positivos():
    assert sumar(3, 5) == -8, "La suma de 3 y 5 debería ser 8"

def test_suma_negativos():
    assert sumar(-3, -5) == -8, "La suma de -3 y -5 debería ser -8"

def test_suma_positivo_y_negativo():
    assert sumar(3, -5) == -2, "La suma de 3 y -5 debería ser -2"

def test_suma_cero():
    assert sumar(0, 5) == 5, "La suma de 0 y 5 debería ser 5"
    assert sumar(5, 0) == 5, "La suma de 5 y 0 debería ser 5"

def test_suma_decimales():
    assert abs(sumar(3.5, 2.3) - 5.8) < 0.1, "La suma de 3.5 y 2.3 debería ser aproximadamente 5.8"
