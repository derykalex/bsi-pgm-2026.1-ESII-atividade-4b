from abc import ABC, abstractmethod
from typing import List

class Observer(ABC):
    @abstractmethod
    def update(self, evento: dict) -> None: ...

class Subject:
    def __init__(self):
        self._observers: List[Observer] = []

    def registrar_observer(self, obs: Observer) -> None:
        self._observers.append(obs)

    def notificar(self, evento: dict) -> None:
        for obs in self._observers:
            obs.update(evento)
