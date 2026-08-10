from abc import ABC, abstractmethod
from typing import List

from servicos.evento import Evento


class Observer(ABC):
    @abstractmethod
    def update(self, evento: Evento) -> None:
        ...


class Subject:
    def __init__(self):
        self._observers: List[Observer] = []

    def registrar_observer(self, obs: Observer) -> None:
        self._observers.append(obs)

    def notificar(self, evento: Evento) -> None:
        for obs in self._observers:
            obs.update(evento)
