import pytest
from datetime import date, timedelta
from repositorios.interfaces import IRepositorioEmprestimo
from servicos.observer import Observer
from servicos.servico_emprestimo import ServicoEmprestimo
from modelos.equipamento_factory import EquipamentoFactory


# Fake: repositório para testes
class RepositorioFake(IRepositorioEmprestimo):
    def __init__(self):
        criar = EquipamentoFactory.criar_equipamento
        self.equipamentos = [
            criar("notebook", 1, "Notebook Dell"),
            criar("projetor", 2, "Projetor Epson"),
            criar("tablet", 3, "Tablet Samsung")
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


# Spy: agora é um Observer
class NotificadorSpy(Observer):
    def __init__(self):
        self.eventos = []

    def update(self, evento):
        self.eventos.append(evento)


@pytest.fixture
def repositorio_fake():
    return RepositorioFake()


@pytest.fixture
def notificador_spy():
    return NotificadorSpy()


@pytest.fixture
def servico(repositorio_fake, notificador_spy):
    s = ServicoEmprestimo(repositorio_fake)
    s.registrar_observer(notificador_spy)
    return s
