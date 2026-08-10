import pytest

from modelos.equipamento_factory import EquipamentoFactory


@pytest.mark.parametrize("tipo, dias, esperado", [
    ("notebook", 3, 30.0),
    ("notebook", 0, 0.0),
    ("notebook", -5, 0.0),
    ("projetor", 2, 30.0),
    ("projetor", 0, 0.0),
    ("tablet", 5, 50.0),
    ("tablet", 0, 0.0),
    ("tablet", -2, 0.0),
])
def test_calcular_multa_atraso(tipo, dias, esperado):
    equipamento = EquipamentoFactory.criar_equipamento(tipo, 999, "Teste")
    assert equipamento.calcular_multa(dias) == esperado
