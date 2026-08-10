from datetime import date

from modelos.estrategias.multas import (
    MultaComCarencia,
    MultaDiariaPadrao,
)
from servicos.evento import Evento
from servicos.notificador import Notificador
from servicos.observadores import Notificador as NotificadorObserver
from servicos.observadores import Observador


def test_multa_diaria_padrao_sem_atraso():
    estrategia = MultaDiariaPadrao()

    assert estrategia.calcular(0) == 0.0


def test_multa_diaria_padrao_com_atraso():
    estrategia = MultaDiariaPadrao(valor_por_dia=10.0)

    assert estrategia.calcular(3) == 30.0


def test_multa_diaria_padrao_atraso_negativo():
    estrategia = MultaDiariaPadrao(valor_por_dia=10.0)

    assert estrategia.calcular(-2) == 0.0


def test_multa_com_carencia_dentro_da_carencia():
    estrategia = MultaComCarencia(
        valor_por_dia=10.0,
        carencia_dias=2,
    )

    assert estrategia.calcular(1) == 0.0


def test_multa_com_carencia_no_limite():
    estrategia = MultaComCarencia(
        valor_por_dia=10.0,
        carencia_dias=2,
    )

    assert estrategia.calcular(2) == 0.0


def test_multa_com_carencia_com_atraso():
    estrategia = MultaComCarencia(
        valor_por_dia=10.0,
        carencia_dias=2,
    )

    assert estrategia.calcular(5) == 30.0


def test_notificador_emprestimo(capsys):
    notificador = Notificador.__new__(Notificador)

    evento = Evento(
        tipo="emprestimo",
        email="usuario@ufra.edu.br",
        data=date(2026, 8, 10),
    )

    notificador.notificar(evento)

    saida = capsys.readouterr().out

    assert "[EMAIL] Empréstimo registrado" in saida
    assert "usuario@ufra.edu.br" in saida


def test_notificador_devolucao(capsys):
    notificador = Notificador.__new__(Notificador)

    evento = Evento(
        tipo="devolucao",
        email="usuario@ufra.edu.br",
    )

    notificador.notificar(evento)

    saida = capsys.readouterr().out

    assert "Devolução registrada com sucesso" in saida
    assert "usuario@ufra.edu.br" in saida


def test_notificador_atraso(capsys):
    notificador = Notificador.__new__(Notificador)

    evento = Evento(
        tipo="atraso",
        email="usuario@ufra.edu.br",
    )

    notificador.notificar(evento)

    saida = capsys.readouterr().out

    assert "empréstimo em atraso" in saida
    assert "usuario@ufra.edu.br" in saida


class ObservadorTeste(Observador):
    def __init__(self):
        self.evento = None
        self.dados = None

    def atualizar(self, evento: str, dados: dict):
        self.evento = evento
        self.dados = dados


def test_observador_recebe_notificacao():
    notificador = NotificadorObserver()
    observador = ObservadorTeste()

    notificador.adicionar_observador(observador)

    dados = {
        "email": "usuario@ufra.edu.br",
        "id": 1,
    }

    notificador.notificar("emprestimo", dados)

    assert observador.evento == "emprestimo"
    assert observador.dados == dados


def test_observador_pode_ser_removido():
    notificador = NotificadorObserver()
    observador = ObservadorTeste()

    notificador.adicionar_observador(observador)
    notificador.remover_observador(observador)

    notificador.notificar("emprestimo", {"id": 1})

    assert observador.evento is None
    assert observador.dados is None


def test_varios_observadores_recebem_evento():
    notificador = NotificadorObserver()

    primeiro = ObservadorTeste()
    segundo = ObservadorTeste()

    notificador.adicionar_observador(primeiro)
    notificador.adicionar_observador(segundo)

    dados = {"id": 10}

    notificador.notificar("devolucao", dados)

    assert primeiro.evento == "devolucao"
    assert segundo.evento == "devolucao"
    assert primeiro.dados == dados
    assert segundo.dados == dados
