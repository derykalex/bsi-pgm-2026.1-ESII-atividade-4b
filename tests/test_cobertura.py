from datetime import date, timedelta

import pytest

from app.sistema import SistemaDeEmprestimos
from modelos.emprestimo import Emprestimo
from modelos.equipamento_factory import EquipamentoFactory
from repositorios.repositorio_emprestimo import RepositorioEmprestimo
from servicos.evento import Evento
from servicos.notificador_email import NotificadorEmail


def test_factory_cria_todos_os_tipos_de_equipamento():
    notebook = EquipamentoFactory.criar_equipamento(
        "notebook",
        1,
        "Notebook"
    )

    projetor = EquipamentoFactory.criar_equipamento(
        "projetor",
        2,
        "Projetor"
    )

    tablet = EquipamentoFactory.criar_equipamento(
        "tablet",
        3,
        "Tablet"
    )

    assert notebook.tipo == "notebook"
    assert projetor.tipo == "projetor"
    assert tablet.tipo == "tablet"


def test_factory_aceita_nomes_completos():
    notebook = EquipamentoFactory.criar_equipamento(
        "Notebook Dell",
        1,
        "Notebook Dell"
    )

    projetor = EquipamentoFactory.criar_equipamento(
        "Projetor Epson",
        2,
        "Projetor Epson"
    )

    tablet = EquipamentoFactory.criar_equipamento(
        "Tablet Samsung",
        3,
        "Tablet Samsung"
    )

    assert notebook.tipo == "notebook"
    assert projetor.tipo == "projetor"
    assert tablet.tipo == "tablet"


def test_factory_rejeita_tipo_desconhecido():
    with pytest.raises(ValueError):
        EquipamentoFactory.criar_equipamento(
            "computador",
            99,
            "Computador"
        )


def test_repositorio_busca_equipamento_existente():
    repositorio = RepositorioEmprestimo()

    equipamento = repositorio.buscar_equipamento(1)

    assert equipamento is not None
    assert equipamento.id == 1


def test_repositorio_retorna_none_para_equipamento_inexistente():
    repositorio = RepositorioEmprestimo()

    equipamento = repositorio.buscar_equipamento(999)

    assert equipamento is None


def test_repositorio_controla_disponibilidade():
    repositorio = RepositorioEmprestimo()

    repositorio.marcar_indisponivel(1)

    equipamento = repositorio.buscar_equipamento(1)

    assert equipamento.disponivel is False

    repositorio.marcar_disponivel(1)

    assert equipamento.disponivel is True


def test_repositorio_ignora_equipamento_inexistente():
    repositorio = RepositorioEmprestimo()

    repositorio.marcar_indisponivel(999)
    repositorio.marcar_disponivel(999)

    assert repositorio.buscar_equipamento(999) is None


def test_repositorio_salva_e_busca_emprestimo():
    repositorio = RepositorioEmprestimo()

    emprestimo = Emprestimo(
        id=1,
        equipamento_id=1,
        usuario_nome="Maria",
        usuario_email="maria@test.com",
        data_emprestimo=date.today(),
        data_devolucao=date.today() + timedelta(days=7)
    )

    repositorio.salvar_emprestimo(emprestimo)

    encontrado = repositorio.buscar_emprestimo(1)

    assert encontrado is not None
    assert encontrado.usuario_nome == "Maria"


def test_repositorio_retorna_none_para_emprestimo_inexistente():
    repositorio = RepositorioEmprestimo()

    assert repositorio.buscar_emprestimo(999) is None


def test_repositorio_marca_emprestimo_como_devolvido():
    repositorio = RepositorioEmprestimo()

    emprestimo = Emprestimo(
        id=1,
        equipamento_id=1,
        usuario_nome="João",
        usuario_email="joao@test.com",
        data_emprestimo=date.today(),
        data_devolucao=date.today() + timedelta(days=7)
    )

    repositorio.salvar_emprestimo(emprestimo)
    repositorio.marcar_devolvido(1)

    assert emprestimo.devolvido is True


def test_repositorio_ignora_devolucao_inexistente():
    repositorio = RepositorioEmprestimo()

    repositorio.marcar_devolvido(999)

    assert repositorio.buscar_emprestimo(999) is None


def test_repositorio_calcula_proximo_id():
    repositorio = RepositorioEmprestimo()

    assert repositorio.proximo_id_emprestimo() == 1


def test_repositorio_lista_emprestimos_em_atraso():
    repositorio = RepositorioEmprestimo()

    emprestimo = Emprestimo(
        id=1,
        equipamento_id=1,
        usuario_nome="Carlos",
        usuario_email="carlos@test.com",
        data_emprestimo=date.today() - timedelta(days=10),
        data_devolucao=date.today() - timedelta(days=3)
    )

    repositorio.salvar_emprestimo(emprestimo)

    atrasados = repositorio.listar_em_atraso()

    assert len(atrasados) == 1
    assert atrasados[0].id == 1


def test_repositorio_nao_lista_emprestimo_devolvido():
    repositorio = RepositorioEmprestimo()

    emprestimo = Emprestimo(
        id=1,
        equipamento_id=1,
        usuario_nome="Carlos",
        usuario_email="carlos@test.com",
        data_emprestimo=date.today() - timedelta(days=10),
        data_devolucao=date.today() - timedelta(days=3),
        devolvido=True
    )

    repositorio.salvar_emprestimo(emprestimo)

    atrasados = repositorio.listar_em_atraso()

    assert atrasados == []


def test_sistema_facade_registra_emprestimo():
    sistema = SistemaDeEmprestimos()

    resultado = sistema.registrar(
        1,
        "Ana",
        "ana@test.com",
        7
    )

    assert resultado is True


def test_sistema_facade_rejeita_equipamento_inexistente():
    sistema = SistemaDeEmprestimos()

    resultado = sistema.registrar(
        999,
        "Ana",
        "ana@test.com",
        7
    )

    assert resultado is False


def test_sistema_facade_registra_e_devolve():
    sistema = SistemaDeEmprestimos()

    registrado = sistema.registrar(
        1,
        "Ana",
        "ana@test.com",
        7
    )

    devolvido = sistema.registrar_devolucao(1)

    assert registrado is True
    assert devolvido is True


def test_sistema_facade_devolucao_inexistente():
    sistema = SistemaDeEmprestimos()

    resultado = sistema.registrar_devolucao(999)

    assert resultado is False


def test_sistema_lista_atrasados():
    sistema = SistemaDeEmprestimos()

    sistema.registrar(
        1,
        "Ana",
        "ana@test.com",
        7
    )

    emprestimo = sistema._repositorio.buscar_emprestimo(1)

    emprestimo.data_devolucao = (
        date.today() - timedelta(days=2)
    )

    atrasados = sistema.listar_atrasados()

    assert len(atrasados) == 1


def test_notificador_processa_evento_de_emprestimo(capsys):
    notificador = NotificadorEmail()

    evento = Evento(
        tipo="emprestimo",
        email="ana@test.com",
        data=date.today()
    )

    notificador.notificar(evento)

    saida = capsys.readouterr().out

    assert "[EMAIL] Empréstimo registrado" in saida


def test_notificador_processa_evento_de_devolucao(capsys):
    notificador = NotificadorEmail()

    evento = Evento(
        tipo="devolucao",
        email="ana@test.com",
        multa=30.0
    )

    notificador.notificar(evento)

    saida = capsys.readouterr().out

    assert "[EMAIL] Devolução registrada" in saida
    assert "30.00" in saida


def test_notificador_processa_evento_de_atraso(capsys):
    notificador = NotificadorEmail()

    evento = Evento(
        tipo="atraso",
        email="ana@test.com",
        multa=20.0
    )

    notificador.notificar(evento)

    saida = capsys.readouterr().out

    assert "[EMAIL] Atraso identificado" in saida
    assert "20.00" in saida


def test_notificador_ignora_evento_desconhecido(capsys):
    notificador = NotificadorEmail()

    evento = Evento(
        tipo="desconhecido",
        email="teste@test.com"
    )

    notificador.notificar(evento)

    saida = capsys.readouterr().out

    assert saida == ""


def test_evento_possui_valores_padrao():
    evento = Evento(
        tipo="teste",
        email="teste@test.com"
    )

    assert evento.tipo == "teste"
    assert evento.email == "teste@test.com"
    assert evento.data is None
    assert evento.multa is None
