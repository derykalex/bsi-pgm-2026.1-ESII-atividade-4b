from repositorios.repositorio_emprestimo import RepositorioEmprestimo
from servicos.servico_emprestimo import ServicoEmprestimo
from servicos.notificador_email import NotificadorEmail


def test_fluxo_registrar_devolver_com_componentes_reais():
    repositorio = RepositorioEmprestimo()
    servico = ServicoEmprestimo(repositorio)
    servico.registrar_observer(NotificadorEmail())

    sucesso = servico.registrar(1, "Ana", "ana@ufra.edu.br", dias=7)
    assert sucesso is True

    emprestimo = repositorio.buscar_emprestimo(1)
    assert emprestimo is not None
    assert emprestimo.equipamento_id == 1
    assert repositorio.buscar_equipamento(1).disponivel is False
