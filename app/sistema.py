# app/sistema.py
"""
Facade (Padrão Estrutural GoF)
Ponto único de entrada para o subsistema de empréstimos.
"""

from repositorios.repositorio_emprestimo import RepositorioEmprestimo
from servicos.notificador import Notificador
from servicos.servico_emprestimo import ServicoEmprestimo


class SistemaDeEmprestimos:
    """Fachada: esconde a montagem do subsistema."""

    def __init__(self):
        self._repositorio = RepositorioEmprestimo()
        self._notificador = Notificador()
        self._servico = ServicoEmprestimo(
            self._repositorio, 
            self._notificador
        )

    def registrar(self, equipamento_id: int, nome: str, email: str, dias: int):
        return self._servico.registrar(equipamento_id, nome, email, dias)

    def registrar_devolucao(self, emprestimo_id: int):
        return self._servico.registrar_devolucao(emprestimo_id)

    def listar_atrasados(self):
        return self._servico.listar_atrasados()
