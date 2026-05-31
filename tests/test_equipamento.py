import pytest
from modelos.equipamento import Notebook, Projetor, Tablet


@pytest.mark.parametrize("equipamento, dias, esperado", [
    (Notebook(1, "Dell", "notebook"), 3, 30.0),
    (Notebook(1, "Dell", "notebook"), 0, 0.0),
    (Notebook(1, "Dell", "notebook"), -5, 0.0),
    (Projetor(2, "Epson", "projetor"), 2, 30.0),
    (Projetor(2, "Epson", "projetor"), 0, 0.0),
    (Tablet(3, "Samsung", "tablet"), 5, 40.0),
    (Tablet(3, "Samsung", "tablet"), 0, 0.0),
    (Tablet(3, "Samsung", "tablet"), -2, 0.0),
])
def test_calcular_multa_atraso_positivo(equipamento, dias, esperado):
    assert equipamento.calcular_multa(dias) == esperado


@pytest.mark.parametrize("equipamento", [
    Notebook(1, "Dell", "notebook"),
    Projetor(2, "Epson", "projetor"),
    Tablet(3, "Samsung", "tablet"),
])
def test_calcular_multa_atraso_negativo_retorna_zero(equipamento):
    assert equipamento.calcular_multa(-10) == 0.0
    assert equipamento.calcular_multa(0) == 0.0
