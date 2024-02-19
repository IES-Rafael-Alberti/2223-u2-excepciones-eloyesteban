import pytest
from src.actividad1 import division

def test_division_valid():
    assert division(8, 2) == 4
    assert division(9, 3) == 3
    assert division(0, 1) == 0

def test_division_invalid_zero_divisor():
    with pytest.raises(ZeroDivisionError):
        division(8, 0)

def test_division_invalid_value_type():
    with pytest.raises(TypeError):
        division("8", 2)

    with pytest.raises(TypeError):
        division(8, "2")

    with pytest.raises(TypeError):
        division("8", "2")
