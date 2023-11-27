import pytest
from src.ejercicios_3_1_2 import llamarAsignaturas

@pytest.mark.parametrize(
    "input_n1, input_n2, expected",
    [
        ("F", "O", "A"),
        ("M", "E", "B"),
        ("M", "P", "A")
       
    ]
)
def test_llamarAsignaturas_params(input_n1, input_n2,expected):
    assert llamarAsignaturas(input_n1, input_n2) == expected
    