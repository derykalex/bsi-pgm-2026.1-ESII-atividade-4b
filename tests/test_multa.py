from multa import calcular_desconto_antecipado, calcular_multa_com_carencia


def test_atraso_zero_nao_gera_multa():
    multa = calcular_multa_com_carencia(dias_atraso=0, valor_dia=10.0, carencia=2)
    assert multa == 0.0


def test_cobra_dias_excedentes_alem_da_carencia():
    multa = calcular_multa_com_carencia(dias_atraso=5, valor_dia=10.0, carencia=2)
    assert multa == 30.0


def test_atraso_dentro_da_carencia_nao_gera_multa_negativa():
    multa = calcular_multa_com_carencia(dias_atraso=1, valor_dia=10.0, carencia=2)
    assert multa == 0.0


def test_devolucao_antecipada_gera_desconto():
    desconto = calcular_desconto_antecipado(dias_adiantados=3, valor_dia=5.0)
    assert desconto == 15.0


def test_devolucao_antecipada_maior_desconto():
    desconto = calcular_desconto_antecipado(dias_adiantados=5, valor_dia=8.0)
    assert desconto == 40.0


def test_devolucao_sem_adiantamento_nao_gera_desconto_negativo():
    desconto = calcular_desconto_antecipado(dias_adiantados=-2, valor_dia=10.0)
    assert desconto == 0.0
