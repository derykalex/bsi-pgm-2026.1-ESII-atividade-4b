def calcular_multa_com_carencia(dias_atraso, valor_dia, carencia):
    if dias_atraso <= carencia:
        return 0.0
    return (dias_atraso - carencia) * valor_dia
