# Equipamento: representar dados de equipamento.
from dataclasses import dataclass

@dataclass
class Equipamento:
    id: int
    nome: str
    tipo: str
    disponivel: bool = True
