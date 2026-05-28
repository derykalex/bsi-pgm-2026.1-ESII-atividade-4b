from servicos.servico_emprestimo import ServicoEmprestimo


class RepositorioFalso:

    def __init__(self):
        self.emprestimos = []

    def buscar_equipamento(self, equip_id):
        return type(
            "Equipamento",
            (),
            {
                "id": 1,
                "disponivel": True
            }
        )()

    def salvar_emprestimo(self, emprestimo):
        self.emprestimos.append(emprestimo)

    def marcar_indisponivel(self, equip_id):
        pass


class NotificadorFalso:

    def notificar_emprestimo(self, email, data):
        pass


def test_registrar_retorna_true_quando_equipamento_disponivel():

    repo = RepositorioFalso()
    notif = NotificadorFalso()

    servico = ServicoEmprestimo(repo, notif)

    resultado = servico.registrar(
        1,
        "Alex",
        "alex@email.com",
        7
    )

    assert resultado is True
