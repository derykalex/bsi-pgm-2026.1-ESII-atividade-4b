from repositorios.repositorio_emprestimo import RepositorioEmprestimo
from servicos.notificador_email import NotificadorEmail   # Use o que realmente funciona
from servicos.servico_emprestimo import ServicoEmprestimo


def test_fluxo_registrar_devolver_com_componentes_reais():
    """Teste de integração com componentes reais"""
    # Arrange
    repositorio = RepositorioEmprestimo()
    notificador = NotificadorEmail()   # ← Mudança aqui
    servico = ServicoEmprestimo(repositorio, notificador)

    # Act
    sucesso = servico.registrar(1, "Ana", "ana@ufra.edu.br", dias=7)

    # Assert
    assert sucesso is True
    emprestimo = repositorio.buscar_emprestimo(1)
    assert emprestimo is not None
    assert emprestimo.equipamento_id == 1
    assert repositorio.buscar_equipamento(1).disponivel is False
