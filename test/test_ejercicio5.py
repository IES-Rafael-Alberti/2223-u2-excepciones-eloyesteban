import pytest
from src.ejercicio5 import verificar_contraseña 

def test_contraseña_correcta():
    assert verificar_contraseña("contraseña") == True

def test_contraseña_incorrecta():
    with pytest.raises(NameError, match="Contraseña Incorrecta!!"):
        verificar_contraseña("Forzar_Error")