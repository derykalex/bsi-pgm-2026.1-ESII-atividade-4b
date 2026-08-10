from datetime import date, timedelta


def test_registrar_devolve_true_quando_equipamento_disponivel(
    servico,
    repositorio_fake
):
    resultado = servico.registrar(
        1,
        "Ana",
        "ana@test.com",
        7
    )

    assert resultado is True


def test_registrar_devolve_false_quando_equipamento_indisponivel(
    servico,
    repositorio_fake
):
    repositorio_fake.marcar_indisponivel(1)

    resultado = servico.registrar(
        1,
        "Ana",
        "ana@test.com",
        7
    )

    assert resultado is False


def test_registrar_notifica_usuario_apos_sucesso(
    servico,
    notificador_spy
):
    servico.registrar(
        1,
        "Ana",
        "ana@test.com",
        7
    )

    assert len(notificador_spy.eventos) == 1

    evento = notificador_spy.eventos[0]

    assert evento.tipo == "emprestimo"
    assert evento.email == "ana@test.com"


def test_devolver_calcula_multa_correta_para_atraso(
    servico,
    repositorio_fake,
    notificador_spy
):
    servico.registrar(
        1,
        "Ana",
        "ana@test.com",
        7
    )

    emprestimo = repositorio_fake.buscar_emprestimo(1)

    emprestimo.data_devolucao = (
        date.today() - timedelta(days=3)
    )

    sucesso = servico.registrar_devolucao(1)

    assert sucesso is True

    assert len(notificador_spy.eventos) == 2

    evento_emprestimo = notificador_spy.eventos[0]
    evento_devolucao = notificador_spy.eventos[1]

    assert evento_emprestimo.tipo == "emprestimo"
    assert evento_devolucao.tipo == "devolucao"
    assert evento_devolucao.email == "ana@test.com"
    assert evento_devolucao.multa == 30.0


def test_devolver_marca_equipamento_como_disponivel(
    servico,
    repositorio_fake
):
    servico.registrar(
        1,
        "Ana",
        "ana@test.com",
        7
    )

    servico.registrar_devolucao(1)

    equipamento = repositorio_fake.buscar_equipamento(1)

    assert equipamento.disponivel is True


def test_devolver_falha_silenciosamente_para_emprestimo_inexistente(
    servico
):
    resultado = servico.registrar_devolucao(999)

    assert resultado is False


def test_listar_atrasados_notifica_evento_de_atraso(
    servico,
    repositorio_fake,
    notificador_spy
):
    servico.registrar(
        1,
        "Ana",
        "ana@test.com",
        7
    )

    emprestimo = repositorio_fake.buscar_emprestimo(1)

    emprestimo.data_devolucao = (
        date.today() - timedelta(days=2)
    )

    servico.listar_atrasados()

    assert len(notificador_spy.eventos) == 2

    evento_emprestimo = notificador_spy.eventos[0]
    evento_atraso = notificador_spy.eventos[1]

    assert evento_emprestimo.tipo == "emprestimo"
    assert evento_atraso.tipo == "atraso"
    assert evento_atraso.email == "ana@test.com"
    assert evento_atraso.multa == 20.0
