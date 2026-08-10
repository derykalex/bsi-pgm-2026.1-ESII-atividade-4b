from servicos.evento import Evento


class ServicoEmprestimo:
    def __init__(self, repositorio, notificador):
        self.repositorio = repositorio
        self.notificador = notificador

    def registrar(self, equipamento_id, usuario_nome, usuario_email, dias):
        equipamento = self.repositorio.buscar_equipamento(equipamento_id)

        if equipamento is None:
            raise ValueError("Equipamento não encontrado.")

        if not equipamento.disponivel:
            raise ValueError("Equipamento indisponível.")

        emprestimo = self.repositorio.criar_emprestimo(
            equipamento,
            usuario_nome,
            usuario_email,
            dias
        )

        equipamento.disponivel = False
        self.repositorio.salvar_equipamento(equipamento)

        evento = Evento(
            tipo="emprestimo",
            email=usuario_email,
            data=emprestimo.data_devolucao
        )

        self.notificador.notificar(evento)

        return emprestimo

    def registrar_devolucao(self, emprestimo_id):
        emprestimo = self.repositorio.buscar_emprestimo(emprestimo_id)

        if emprestimo is None:
            raise ValueError("Empréstimo não encontrado.")

        multa = emprestimo.calcular_multa()

        emprestimo.devolvido = True

        equipamento = self.repositorio.buscar_equipamento(
            emprestimo.equipamento_id
        )

        if equipamento is not None:
            equipamento.disponivel = True
            self.repositorio.salvar_equipamento(equipamento)

        self.repositorio.salvar_emprestimo(emprestimo)

        evento = Evento(
            tipo="devolucao",
            email=emprestimo.usuario_email,
            multa=multa
        )

        self.notificador.notificar(evento)

        return multa

    def listar_atrasados(self):
        emprestimos = self.repositorio.listar_emprestimos()

        atrasados = []

        for emprestimo in emprestimos:
            dias_atraso = emprestimo.dias_atraso()

            if dias_atraso > 0:
                multa_calculada = emprestimo.calcular_multa()

                atrasados.append(emprestimo)

                self._imprimir_linha_atraso(
                    emprestimo,
                    dias_atraso,
                    multa_calculada
                )

                evento = Evento(
                    tipo="atraso",
                    email=emprestimo.usuario_email,
                    multa=multa_calculada
                )

                self.notificador.notificar(evento)

        return atrasados

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
