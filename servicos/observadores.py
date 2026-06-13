from abc import ABC, abstractmethod
from typing import List


class Observador(ABC):
    """Observer: Interface para quem quer ser notificado"""

    @abstractmethod
    def atualizar(self, evento: str, dados: dict):
        pass


class Notificador:
    """Subject - Gerencia os observers"""

    def __init__(self):
        self._observadores: List[Observador] = []

    def adicionar_observador(self, observador: Observador):
        self._observadores.append(observador)

    def remover_observador(self, observador: Observador):
        self._observadores.remove(observador)

    def notificar(self, evento: str, dados: dict):
        for obs in self._observadores:
            obs.atualizar(evento, dados)
