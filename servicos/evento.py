# servicos/evento.py
"""
Evento: substitui o dict primitivo (Primitive Obsession) - Aula 12
"""

from dataclasses import dataclass
from datetime import date


@dataclass
class Evento:
    tipo: str
    email: str
    data: date | None = None      # usado no empréstimo
    multa: float | None = None    # usado na devolução
