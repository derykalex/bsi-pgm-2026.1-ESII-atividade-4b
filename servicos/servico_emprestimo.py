# ServicoEmprestimo: regras de negócio.

from datetime import date, timedelta

from modelos.emprestimo import Emprestimo
from repositorios.interfaces import IRepositorioEmprestimo
from servicos.interfaces import INotificador
from servicos.evento import Evento


class ServicoEmprestimo:

    def __init__(self, repositorio: IRepositorioEmprestimo, notificador: INotificador):
        """DIP aplicado: dependências são injetadas via construtor"""
        self.repositorio = repositorio
        self.notificador = notificador

    def registrar(self, equipamento_id: int, usuario_nome: str, usuario_email: str, dias: int):
        equipamento = self.repositorio.buscar_equipamento(equipamento_id)

        if not equipamento or not equipamento.disponivel:
            return False

        emprestimo = Emprestimo(
            id=self.repositorio.proximo_id_emprestimo(),
            equipamento_id=equipamento_id,
            usuario_nome=usuario_nome,
            usuario_email=usuario_email,
            data_emprestimo=date.today(),
            data_devolucao=date.today() + timedelta(days=dias)
        )

        self.repositorio.salvar_emprestimo(emprestimo)
        self.repositorio.marcar_indisponivel(equipamento_id)

        self.notificador.notificar(
            Evento("emprestimo", usuario_email, data=emprestimo.data_devolucao)
        )

        return True

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
                self.notificador.notificar(Evento("atraso", emprestimo.usuario_email))

        self.repositorio.marcar_devolvido(emprestimo_id)
        self.repositorio.marcar_disponivel(emprestimo.equipamento_id)

        self.notificador.notificar(
            Evento("devolucao", emprestimo.usuario_email, multa=multa)
        )

        return True

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

            self._imprimir_linha_atraso(emprestimo, dias_atraso, multa)
            self.notificador.notificar(Evento("atraso", emprestimo.usuario_email))

    def _imprimir_linha_atraso(self, emprestimo, dias_atraso: int, multa: float):
        """Método extraído (Extract Function) - Aula 12"""
        print(
            f"ID: {emprestimo.id} | Usuário: {emprestimo.usuario_nome} | "
            f"Email: {emprestimo.usuario_email} | Devolução prevista: {emprestimo.data_devolucao} | "
            f"Dias atraso: {dias_atraso} | Multa: R${multa:.2f}"
        )
