import pytest
from src.ejercicio4 import obtener_numero_entero

def test_numero_entero_valido():
    assert obtener_numero_entero(5) == 5

def test_numero_entero_invalido():
    with pytest.raises(ValueError, match="La entrada no es correcta"):
        obtener_numero_entero("sljlafjsl")
