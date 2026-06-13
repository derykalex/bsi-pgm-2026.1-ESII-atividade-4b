from abc import ABC, abstractmethod
from dataclasses import dataclass


class EstrategiaMulta(ABC):
    """Strategy: Interface para diferentes algoritmos de cálculo de multa"""

    @abstractmethod
    def calcular(self, dias_atraso: int) -> float:
        pass


@dataclass
class MultaDiariaPadrao(EstrategiaMulta):
    valor_por_dia: float = 10.0

    def calcular(self, dias_atraso: int) -> float:
        return max(0.0, dias_atraso * self.valor_por_dia)


@dataclass
class MultaComCarencia(EstrategiaMulta):
    valor_por_dia: float = 10.0
    carencia_dias: int = 2

    def calcular(self, dias_atraso: int) -> float:
        dias_cobraveis = max(0, dias_atraso - self.carencia_dias)
        return round(dias_cobraveis * self.valor_por_dia, 2)
