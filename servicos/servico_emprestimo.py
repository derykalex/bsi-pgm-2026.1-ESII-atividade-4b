# ServicoEmprestimo: regras de negócio.
from datetime import date, timedelta

from modelos.emprestimo import Emprestimo
from repositorios.repositorio_emprestimo import RepositorioEmprestimo
from servicos.notificador import Notificador


class ServicoEmprestimo:

    def __init__(self):
        self.repositorio = RepositorioEmprestimo()
        self.notificador = Notificador()

    # UC01 — Registrar empréstimo
    def registrar(self, equip_id: int, nome: str, email: str, dias: int):

        equipamento = self.repositorio.buscar_equipamento(equip_id)

        if not equipamento:
            return False

        if not equipamento.disponivel:
            return False

        emprestimo = Emprestimo(
            id=len(self.repositorio.emprestimos) + 1,
            equipamento_id=equip_id,
            nome_usuario=nome,
            email_usuario=email,
            data_emprestimo=date.today(),
            data_devolucao=date.today() + timedelta(days=dias)
        )

        self.repositorio.salvar_emprestimo(emprestimo)
        self.repositorio.marcar_indisponivel(equip_id)

        self.notificador.notificar_emprestimo(
            email,
            emprestimo.data_devolucao
        )

        return True

    # UC02 — Registrar devolução
    def registrar_devolucao(self, emprestimo_id: int):

        emprestimo = self.repositorio.buscar_emprestimo(emprestimo_id)

        if not emprestimo:
            return False

        if emprestimo.devolvido:
            return False

        hoje = date.today()
        multa = 0

        # Regra didática da atividade (if/elif)
        if hoje > emprestimo.data_devolucao:

            dias_atraso = (hoje - emprestimo.data_devolucao).days

            equipamento = self.repositorio.buscar_equipamento(
                emprestimo.equipamento_id
            )

            if equipamento.tipo == "notebook":
                multa = dias_atraso * 10

            elif equipamento.tipo == "projetor":
                multa = dias_atraso * 15

            elif equipamento.tipo == "tablet":
                multa = dias_atraso * 8

            self.notificador.notificar_atraso(
                emprestimo.email_usuario,
                multa
            )

        self.repositorio.marcar_devolvido(emprestimo_id)
        self.repositorio.marcar_disponivel(
            emprestimo.equipamento_id
        )

        self.notificador.notificar_devolucao(
            emprestimo.email_usuario
        )

        return True

    # UC03 — Listar atrasados
    def listar_atrasados(self):

        atrasados = self.repositorio.buscar_emprestimos_atrasados(
            date.today()
        )

        if not atrasados:
            print("Nenhum empréstimo em atraso.")
            return

        print("\n=== EMPRÉSTIMOS EM ATRASO ===")

        for emprestimo in atrasados:
            print(
                f"ID: {emprestimo.id} | "
                f"Usuário: {emprestimo.nome_usuario} | "
                f"Email: {emprestimo.email_usuario} | "
                f"Devolução prevista: {emprestimo.data_devolucao}"
            )
