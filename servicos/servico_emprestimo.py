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
            usuario_nome=nome,
            usuario_email=email,
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

        # OCP aplicado: cada equipamento calcula sua própria multa
        if hoje > emprestimo.data_devolucao:

            dias_atraso = (hoje - emprestimo.data_devolucao).days

            equipamento = self.repositorio.buscar_equipamento(
                emprestimo.equipamento_id
            )

            multa = equipamento.calcular_multa(dias_atraso)

            self.notificador.notificar_atraso(
                emprestimo.usuario_email,
                multa
            )

        self.repositorio.marcar_devolvido(emprestimo_id)
        self.repositorio.marcar_disponivel(
            emprestimo.equipamento_id
        )

        self.notificador.notificar_devolucao(
            emprestimo.usuario_email
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

            dias_atraso = (
                date.today() - emprestimo.data_devolucao
            ).days

            equipamento = self.repositorio.buscar_equipamento(
                emprestimo.equipamento_id
            )

            multa = equipamento.calcular_multa(dias_atraso)

            print(
                f"ID: {emprestimo.id} | "
                f"Usuário: {emprestimo.usuario_nome} | "
                f"Email: {emprestimo.usuario_email} | "
                f"Devolução prevista: {emprestimo.data_devolucao} | "
                f"Dias atraso: {dias_atraso} | "
                f"Multa: R${multa:.2f}"
            )

            self.notificador.notificar_atraso(
                emprestimo.usuario_email,
                multa
            )
