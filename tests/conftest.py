import pytest
from datetime import date

from modelos.equipamento import Notebook, Projetor, Tablet
from modelos.multa_strategy import MultaPorDia
from repositorios.interfaces import IRepositorioEmprestimo
from servicos.interfaces import INotificador
from servicos.servico_emprestimo import ServicoEmprestimo
from servicos.evento import Evento


class RepositorioFake(IRepositorioEmprestimo):
    def __init__(self):
        multa_padrao = MultaPorDia(10.0)
        self.equipamentos = [
            Notebook(id=1, nome="Notebook Dell", tipo="notebook", multa=multa_padrao),
            Projetor(id=2, nome="Projetor Epson", tipo="projetor", multa=MultaPorDia(15.0)),
            Tablet(id=3, nome="Tablet Samsung", tipo="tablet", multa=multa_padrao)
        ]
        self.emprestimos = []

    def buscar_equipamento(self, equip_id):
        return next((e for e in self.equipamentos if e.id == equip_id), None)

    def salvar_emprestimo(self, emprestimo):
        self.emprestimos.append(emprestimo)

    def buscar_emprestimo(self, emprestimo_id):
        return next((e for e in self.emprestimos if e.id == emprestimo_id), None)

    def marcar_indisponivel(self, equip_id):
        equip = self.buscar_equipamento(equip_id)
        if equip:
            equip.disponivel = False

    def marcar_disponivel(self, equip_id):
        equip = self.buscar_equipamento(equip_id)
        if equip:
            equip.disponivel = True

    def marcar_devolvido(self, emprestimo_id):
        emp = self.buscar_emprestimo(emprestimo_id)
        if emp:
            emp.devolvido = True

    def listar_em_atraso(self):
        hoje = date.today()
        return [e for e in self.emprestimos if not e.devolvido and e.data_devolucao < hoje]

    def proximo_id_emprestimo(self):
        return len(self.emprestimos) + 1


class NotificadorSpy(INotificador):
    def __init__(self):
        self.eventos = []

    def notificar(self, evento: Evento):
        """Método compatível com o que ServicoEmprestimo chama"""
        self.eventos.append(evento)

    # Métodos abstratos obrigatórios (para satisfazer INotificador)
    def notificar_emprestimo(self, email, data_devolucao):
        self.notificar(Evento("emprestimo", email, data=data_devolucao))

    def notificar_devolucao(self, email, multa):
        self.notificar(Evento("devolucao", email, multa=multa))

    def notificar_atraso(self, email):
        self.notificar(Evento("atraso", email))


@pytest.fixture
def repositorio_fake():
    return RepositorioFake()

@pytest.fixture
def notificador_spy():
    return NotificadorSpy()

@pytest.fixture
def servico(repositorio_fake, notificador_spy):
    return ServicoEmprestimo(repositorio_fake, notificador_spy)
