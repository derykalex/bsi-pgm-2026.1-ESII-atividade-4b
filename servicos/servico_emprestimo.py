from datetime import date, timedelta

from modelos.emprestimo import Emprestimo
from servicos.evento import Evento


class ServicoEmprestimo:
    def __init__(self, repositorio, notificador):
        self.repositorio = repositorio
        self.notificador = notificador

    def registrar(
        self,
        equipamento_id,
        usuario_nome,
        usuario_email,
        dias
    ):
        equipamento = self.repositorio.buscar_equipamento(
            equipamento_id
        )

        if equipamento is None:
            return False

        if not equipamento.disponivel:
            return False

        data_emprestimo = date.today()
        data_devolucao = data_emprestimo + timedelta(days=dias)

        emprestimo = Emprestimo(
            id=self.repositorio.proximo_id_emprestimo(),
            equipamento_id=equipamento_id,
            usuario_nome=usuario_nome,
            usuario_email=usuario_email,
            data_emprestimo=data_emprestimo,
            data_devolucao=data_devolucao
        )

        self.repositorio.salvar_emprestimo(
            emprestimo
        )

        self.repositorio.marcar_indisponivel(
            equipamento_id
        )

        evento = Evento(
            tipo="emprestimo",
            email=usuario_email,
            data=data_devolucao
        )

        self.notificador.notificar(evento)

        return True

    def registrar_devolucao(self, emprestimo_id):
        emprestimo = self.repositorio.buscar_emprestimo(
            emprestimo_id
        )

        if emprestimo is None:
            return False

        equipamento = self.repositorio.buscar_equipamento(
            emprestimo.equipamento_id
        )

        if equipamento is None:
            return False

        hoje = date.today()

        dias_atraso = max(
            0,
            (hoje - emprestimo.data_devolucao).days
        )

        multa = equipamento.calcular_multa(
            dias_atraso
        )

        self.repositorio.marcar_devolvido(
            emprestimo_id
        )

        self.repositorio.marcar_disponivel(
            emprestimo.equipamento_id
        )

        evento = Evento(
            tipo="devolucao",
            email=emprestimo.usuario_email,
            multa=multa
        )

        self.notificador.notificar(evento)

        return True

    def listar_atrasados(self):
        emprestimos_atrasados = (
            self.repositorio.listar_em_atraso()
        )

        for emprestimo in emprestimos_atrasados:
            equipamento = self.repositorio.buscar_equipamento(
                emprestimo.equipamento_id
            )

            if equipamento is None:
                continue

            dias_atraso = max(
                0,
                (date.today() - emprestimo.data_devolucao).days
            )

            multa = equipamento.calcular_multa(
                dias_atraso
            )

            self._imprimir_linha_atraso(
                emprestimo,
                dias_atraso,
                multa
            )

            evento = Evento(
                tipo="atraso",
                email=emprestimo.usuario_email,
                multa=multa
            )

            self.notificador.notificar(evento)

        return emprestimos_atrasados

    def _imprimir_linha_atraso(
        self,
        emprestimo,
        dias_atraso,
        multa
    ):
        print(
            f"Usuário {emprestimo.usuario_nome} "
            f"está atrasado {dias_atraso} dia(s). "
            f"Multa: R${multa:.2f}"
        )
