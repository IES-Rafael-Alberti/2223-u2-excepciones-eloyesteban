import pytest
from src.actividad2 import conversion

def test_conversion_valid():
    assert conversion(32) == 0  
    assert conversion(212) == 100  
    assert conversion(-40) == -40  

def test_conversion_invalid_low_temp():
    with pytest.raises(ValueError, match="Temperatura Fahrenheit incorrecta: -460"):
        conversion(-460)

def test_conversion_invalid_value_type():
    with pytest.raises(TypeError):
        conversion("no valido")

