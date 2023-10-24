import pytest
from src.ejercicio3 import cuenta_atras

def test_cuenta_atras():
    assert cuenta_atras(5) == "5, 4, 3, 2, 1, 0"

def test_numero_impar_invalid_value_type():
    with pytest.raises(TypeError):
        cuenta_atras("a")