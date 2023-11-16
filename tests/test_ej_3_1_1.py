import pytest
from src.ejercicios_3_1_1 import asignarGrupo

@pytest.mark.parametrize(
    "input_n1, input_n2, expected",
    [
        ("F", "O", "A"),
        ("M", "E", "B"),
        ("M", "P", "A")
       
    ]
)
def test_asignarGrupo_params(input_n1, input_n2,expected):
    assert asignarGrupo(input_n1, input_n2) == expected
    