from abc import ABC, abstractmethod

class EstrategiaMulta(ABC):
    """Strategy: interface para diferentes cálculos de multa"""

    @abstractmethod
    def calcular(self, dias_atraso: int) -> float:
        pass


class MultaDiariaPadrao(EstrategiaMulta):
    """Multa simples por dia (usada atualmente)"""

    def __init__(self, valor_por_dia: float = 10.0):
        self.valor_por_dia = valor_por_dia

    def calcular(self, dias_atraso: int) -> float:
        return max(0.0, dias_atraso * self.valor_por_dia)


class MultaComCarencia(EstrategiaMulta):
    """Multa só cobra após período de carência"""

    def __init__(self, valor_por_dia: float = 10.0, carencia: int = 2):
        self.valor_por_dia = valor_por_dia
        self.carencia = carencia

    def calcular(self, dias_atraso: int) -> float:
        dias_cobraveis = max(0, dias_atraso - self.carencia)
        return round(dias_cobraveis * self.valor_por_dia, 2)
