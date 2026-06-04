def calcular_multa_com_carencia(dias_atraso: int, valor_dia: float, carencia: int) -> float:
    """
    Calcula a multa por atraso com período de carência.
    A multa nunca pode ser negativa.
    """
    dias_cobraveis = max(0, dias_atraso - carencia)
    multa = dias_cobraveis * valor_dia
    return round(multa, 2)
