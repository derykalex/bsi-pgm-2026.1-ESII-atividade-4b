from repositorios.repositorio_emprestimo import RepositorioEmprestimo
from servicos.servico_emprestimo import ServicoEmprestimo
from servicos.notificador_email import NotificadorEmail

class SistemaDeEmprestimos:
    def __init__(self):
        self._repositorio = RepositorioEmprestimo()
        self._servico = ServicoEmprestimo(self._repositorio)
        self._servico.registrar_observer(NotificadorEmail())

    def registrar(self, equipamento_id, nome, email, dias):
        return self._servico.registrar(equipamento_id, nome, email, dias)

    def registrar_devolucao(self, emprestimo_id):
        return self._servico.registrar_devolucao(emprestimo_id)

    def listar_atrasados(self):
        return self._servico.listar_atrasados()
