def calcular_multa_com_carencia(dias_atraso: int, valor_dia: float, carencia: int) -> float:
    """
    Calcula a multa por atraso com período de carência.
    A multa nunca pode ser negativa.
    """
    dias_cobraveis = max(0, dias_atraso - carencia)
    multa = dias_cobraveis * valor_dia
    return round(multa, 2)


def calcular_desconto_antecipado(dias_adiantados: int, valor_dia: float) -> float:
    """
    Calcula desconto por devolução antecipada.
    Nunca retorna valor negativo.
    """
    dias_adiantados_cobraveis = max(0, dias_adiantados)
    desconto = dias_adiantados_cobraveis * valor_dia
    return round(desconto, 2)
