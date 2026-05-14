# Equipamento: entidade de domínio com OCP (Aula 05)

from dataclasses import dataclass
from abc import ABC, abstractmethod


@dataclass
class Equipamento(ABC):
    id: int
    nome: str
    tipo: str
    disponivel: bool = True

    @abstractmethod
    def calcular_multa(self, dias_atraso: int) -> float:
        pass


@dataclass
class Notebook(Equipamento):
    def calcular_multa(self, dias_atraso: int) -> float:
        return max(0.0, dias_atraso * 10.0)


@dataclass
class Projetor(Equipamento):
    def calcular_multa(self, dias_atraso: int) -> float:
        return max(0.0, dias_atraso * 15.0)


@dataclass
class Tablet(Equipamento):
    def calcular_multa(self, dias_atraso: int) -> float:
        return max(0.0, dias_atraso * 8.0)
