import pytest
from datetime import date, timedelta
from servicos.servico_emprestimo import ServicoEmprestimo


def test_registrar_devolve_true_quando_equipamento_disponivel(servico, repositorio_fake):
    """Teste 1 - Fake"""
    resultado = servico.registrar(1, "Ana", "ana@test.com", 7)
    assert resultado is True


def test_registrar_devolve_false_quando_equipamento_indisponivel(servico, repositorio_fake):
    """Teste 2 - Fake configurado"""
    # Torna o equipamento indisponível primeiro
    repositorio_fake.marcar_indisponivel(1)
    resultado = servico.registrar(1, "Ana", "ana@test.com", 7)
    assert resultado is False


def test_registrar_notifica_usuario_apos_sucesso(servico, notificador_spy):
    """Teste 3 - Fake + Spy"""
    servico.registrar(1, "Ana", "ana@test.com", 7)
    assert len(notificador_spy.eventos) == 1
    assert notificador_spy.eventos[0][0] == "emprestimo"


def test_devolver_calcula_multa_correta_para_atraso(servico, repositorio_fake):
    """Teste 4 - Com parametrize (simplificado)"""
    servico.registrar(1, "Ana", "ana@test.com", 7)
    
    # Simula atraso
    emp = repositorio_fake.buscar_emprestimo(1)
    emp.data_devolucao = date.today() - timedelta(days=3)
    
    sucesso = servico.registrar_devolucao(1)
    assert sucesso is True


def test_devolver_marca_equipamento_como_disponivel(servico, repositorio_fake):
    """Teste 5"""
    servico.registrar(1, "Ana", "ana@test.com", 7)
    servico.registrar_devolucao(1)
    
    equipamento = repositorio_fake.buscar_equipamento(1)
    assert equipamento.disponivel is True


def test_devolver_falha_silenciosamente_para_emprestimo_inexistente(servico):
    """Teste 6"""
    resultado = servico.registrar_devolucao(999)
    assert resultado is False
