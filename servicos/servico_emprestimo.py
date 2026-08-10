from servicos.evento import Evento


class ServicoEmprestimo:
    def __init__(self, repositorio, notificador):
        self.repositorio = repositorio
        self.notificador = notificador

    def registrar(self, equipamento_id, usuario_nome, usuario_email, dias):
        equipamento = self.repositorio.buscar_equipamento(equipamento_id)

        if equipamento is None:
            return False

        if not equipamento.disponivel:
            return False

        emprestimo_id = self.repositorio.proximo_id_emprestimo()

        emprestimo = equipamento.criar_emprestimo(
            emprestimo_id,
            usuario_nome,
            usuario_email,
            dias
        )

        self.repositorio.salvar_emprestimo(emprestimo)
        self.repositorio.marcar_indisponivel(equipamento_id)

        evento = Evento(
            tipo="emprestimo",
            email=usuario_email,
            data=emprestimo.data_devolucao
        )

        self.notificador.notificar(evento)

        return True

    def registrar_devolucao(self, emprestimo_id):
        emprestimo = self.repositorio.buscar_emprestimo(emprestimo_id)

        if emprestimo is None:
            return False

        multa = emprestimo.calcular_multa()

        self.repositorio.marcar_devolvido(emprestimo_id)
        self.repositorio.marcar_disponivel(emprestimo.equipamento_id)

        evento = Evento(
            tipo="devolucao",
            email=emprestimo.usuario_email,
            multa=multa
        )

        self.notificador.notificar(evento)

        return True

    def listar_atrasados(self):
        emprestimos_atrasados = self.repositorio.listar_em_atraso()

        for emprestimo in emprestimos_atrasados:
            dias_atraso = emprestimo.dias_atraso()
            multa = emprestimo.calcular_multa()

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
