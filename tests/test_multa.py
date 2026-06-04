from multa import calcular_multa_com_carencia

def test_atraso_zero_nao_gera_multa():
    multa = calcular_multa_com_carencia(dias_atraso=0, valor_dia=10.0, carencia=2)
    assert multa == 0.0
    
def test_cobra_dias_excedentes_alem_da_carencia():
    multa = calcular_multa_com_carencia(dias_atraso=5, valor_dia=10.0, carencia=2)
    assert multa == 30.0

def test_atraso_dentro_da_carencia_nao_gera_multa_negativa():
    multa = calcular_multa_com_carencia(dias_atraso=1, valor_dia=10.0, carencia=2)
    assert multa == 0.0
