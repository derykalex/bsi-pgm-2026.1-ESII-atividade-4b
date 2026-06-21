from abc import ABC, abstractmethod
from typing import List
from servicos.evento import Evento   # ← Adicionado


class Observer(ABC):
    @abstractmethod
    def update(self, evento: Evento) -> None: ...   # ← Alterado de dict para Evento


class Subject:
    def __init__(self):
        self._observers: List[Observer] = []

    def registrar_observer(self, obs: Observer) -> None:
        self._observers.append(obs)

    def notificar(self, evento: Evento) -> None:   # ← Alterado de dict para Evento
        for obs in self._observers:
            obs.update(evento)
