import pytest
from datetime import date, timedelta
from models.equipamento import Notebook, Projetor, Tablet
from repositorios.interfaces import IRepositorioEmprestimo
from servicos.interfaces import INotificador
from servicos.servico_emprestimo import ServicoEmprestimo


# Fake: implementação funcional em memória
class RepositorioFake(IRepositorioEmprestimo):
    def __init__(self):
        self.equipamentos = [
            Notebook(1, "Notebook Dell", "notebook"),
            Projetor(2, "Projetor Epson", "projetor"),
            Tablet(3, "Tablet Samsung", "tablet")
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


# Spy: registra chamadas
class NotificadorSpy(INotificador):
    def __init__(self):
        self.eventos = []

    def notificar_emprestimo(self, email, data_devolucao):
        self.eventos.append(("emprestimo", email, data_devolucao))

    def notificar_devolucao(self, email, multa):
        self.eventos.append(("devolucao", email, multa))

    def notificar_atraso(self, email):
        self.eventos.append(("atraso", email))


@pytest.fixture
def repositorio_fake():
    return RepositorioFake()

@pytest.fixture
def notificador_spy():
    return NotificadorSpy()

@pytest.fixture
def servico(repositorio_fake, notificador_spy):
    return ServicoEmprestimo(repositorio_fake, notificador_spy)
