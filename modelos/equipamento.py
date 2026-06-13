from dataclasses import dataclass, field
from abc import ABC, abstractmethod
from modelos.estrategias.multas import EstrategiaMulta, MultaDiariaPadrao


@dataclass
class Equipamento(ABC):
    id: int
    nome: str
    tipo: str
    disponivel: bool = True
    _estrategia_multa: EstrategiaMulta = field(default_factory=MultaDiariaPadrao, init=False)

    def definir_estrategia_multa(self, estrategia: EstrategiaMulta):
        self._estrategia_multa = estrategia

    def calcular_multa(self, dias_atraso: int) -> float:
        return self._estrategia_multa.calcular(dias_atraso)


# Subclasses continuam existindo, mas sem calcular_multa
@dataclass
class Notebook(Equipamento):
    pass

@dataclass
class Projetor(Equipamento):
    pass

@dataclass
class Tablet(Equipamento):
    pass
