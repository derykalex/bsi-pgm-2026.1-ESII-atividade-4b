from repositorios.repositorio_emprestimo import RepositorioEmprestimo
from servicos.notificador import Notificador
from servicos.servico_emprestimo import ServicoEmprestimo


def test_fluxo_registrar_devolver_com_componentes_reais():

    repositorio = RepositorioEmprestimo()
    notificador = Notificador()

    servico = ServicoEmprestimo(
        repositorio,
        notificador
    )

    sucesso = servico.registrar(
        1,
        "Ana",
        "ana@ufra.edu.br",
        7
    )

    assert sucesso is True

    emprestimo = repositorio.buscar_emprestimo(1)

    assert emprestimo is not None
