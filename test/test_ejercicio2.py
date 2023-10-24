import pytest
from src.ejercicio2 import numero_impar

def test_numero_impar():
    assert numero_impar(5) == "1, 3, 5"

def test_numero_impar_invalid_value_type():
    with pytest.raises(TypeError):
        numero_impar("a")