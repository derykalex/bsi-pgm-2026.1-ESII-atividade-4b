# ServicoEmprestimo: regras de negócio.

from datetime import date, timedelta

from modelos.emprestimo import Emprestimo
from repositorios.interfaces import IRepositorioEmprestimo
from servicos.interfaces import INotificador


class ServicoEmprestimo:

    def __init__(self, repositorio: IRepositorioEmprestimo, notificador: INotificador):
        """DIP aplicado: dependências são injetadas via construtor"""
        self.repositorio = repositorio
        self.notificador = notificador

    # UC01 — Registrar empréstimo
    def registrar(self, equip_id: int, nome: str, email: str, dias: int):

        equipamento = self.repositorio.buscar_equipamento(equip_id)

        if not equipamento:
            return False

        if not equipamento.disponivel:
            return False

        emprestimo = Emprestimo(
            id=self.repositorio.proximo_id_emprestimo(),
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

        if not emprestimo or emprestimo.devolvido:
            return False

        hoje = date.today()
        multa = 0.0

        if hoje > emprestimo.data_devolucao:
            dias_atraso = (hoje - emprestimo.data_devolucao).days
            equipamento = self.repositorio.buscar_equipamento(emprestimo.equipamento_id)
            if equipamento:
                multa = equipamento.calcular_multa(dias_atraso)
                self.notificador.notificar_atraso(emprestimo.usuario_email)

        self.repositorio.marcar_devolvido(emprestimo_id)
        self.repositorio.marcar_disponivel(emprestimo.equipamento_id)

        self.notificador.notificar_devolucao(emprestimo.usuario_email, multa)

        return True

    # UC03 — Listar atrasados
    def listar_atrasados(self):
        atrasados = self.repositorio.listar_em_atraso()

        if not atrasados:
            print("Nenhum empréstimo em atraso.")
            return

        print("\n=== EMPRÉSTIMOS EM ATRASO ===")

        for emprestimo in atrasados:
            dias_atraso = (date.today() - emprestimo.data_devolucao).days
            equipamento = self.repositorio.buscar_equipamento(emprestimo.equipamento_id)
            multa = equipamento.calcular_multa(dias_atraso) if equipamento else 0.0

            print(
                f"ID: {emprestimo.id} | Usuário: {emprestimo.usuario_nome} | "
                f"Email: {emprestimo.usuario_email} | Devolução prevista: {emprestimo.data_devolucao} | "
                f"Dias atraso: {dias_atraso} | Multa: R${multa:.2f}"
            )

            self.notificador.notificar_atraso(emprestimo.usuario_email)
