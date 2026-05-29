from servicos.servico_emprestimo import ServicoEmprestimo


class RepositorioFalso:

    def __init__(self):
        self.emprestimos = []

    def buscar_equipamento(self, equip_id):
        return type(
            "Equipamento",
            (),
            {
                "id": equip_id,
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


def criar_servico():
    repo = RepositorioFalso()
    notif = NotificadorFalso()
    return ServicoEmprestimo(repo, notif)


def test_registrar_retorna_true_quando_equipamento_disponivel():
    servico = criar_servico()

    resultado = servico.registrar(
        1,
        "Alex",
        "alex@email.com",
        7
    )

    assert resultado is True


def test_registrar_equipamento_diferente():
    servico = criar_servico()

    resultado = servico.registrar(
        2,
        "Maria",
        "maria@email.com",
        5
    )

    assert resultado is True


def test_registrar_outro_usuario():
    servico = criar_servico()

    resultado = servico.registrar(
        3,
        "João",
        "joao@email.com",
        10
    )

    assert resultado is True


def test_servico_instanciado():
    servico = criar_servico()
    assert servico is not None
