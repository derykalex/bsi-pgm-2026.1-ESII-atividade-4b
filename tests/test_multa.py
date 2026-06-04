from multa import calcular_multa_com_carencia

def test_atraso_zero_nao_gera_multa():
    multa = calcular_multa_com_carencia(dias_atraso=0, valor_dia=10.0, carencia=2)
    assert multa == 0.0
