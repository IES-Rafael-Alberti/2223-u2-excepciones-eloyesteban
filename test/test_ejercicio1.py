import pytest
from src.ejercicio1 import repeticion

def test_repeticion():
    assert repeticion(1) == "1"
    assert repeticion(5) == "1\n2\n3\n4\n5"
    assert repeticion(10) == "1\n2\n3\n4\n5\n6\n7\n8\n9\n10"
    assert repeticion(0) == ""

def test_repeticion_invalid_value_type():
    with pytest.raises(TypeError):
        repeticion("a")
