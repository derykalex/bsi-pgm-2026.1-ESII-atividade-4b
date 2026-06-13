from datetime import date
from repositorios.interfaces import IRepositorioEmprestimo
from modelos.fabrica_equipamento import EquipamentoFactory


class RepositorioEmprestimo(IRepositorioEmprestimo):

    def __init__(self):
        # Base inicial simulada - usando Simple Factory (Aula 10)
        criar = EquipamentoFactory.criar_equipamento
        self.equipamentos = [
            criar("notebook", 1, "Notebook Dell"),
            criar("projetor", 2, "Projetor Epson"),
            criar("tablet", 3, "Tablet Samsung")
        ]
        self.emprestimos = []

    def buscar_equipamento(self, equip_id):
        for equipamento in self.equipamentos:
            if equipamento.id == equip_id:
                return equipamento
        return None

    def salvar_emprestimo(self, emprestimo):
        self.emprestimos.append(emprestimo)

    def buscar_emprestimo(self, emprestimo_id):
        for emprestimo in self.emprestimos:
            if emprestimo.id == emprestimo_id:
                return emprestimo
        return None

    def marcar_indisponivel(self, equip_id):
        equipamento = self.buscar_equipamento(equip_id)
        if equipamento:
            equipamento.disponivel = False

    def marcar_disponivel(self, equip_id):
        equipamento = self.buscar_equipamento(equip_id)
        if equipamento:
            equipamento.disponivel = True

    def marcar_devolvido(self, emprestimo_id):
        emprestimo = self.buscar_emprestimo(emprestimo_id)
        if emprestimo:
            emprestimo.devolvido = True

    def buscar_emprestimos_atrasados(self, hoje):
        atrasados = []
        for emprestimo in self.emprestimos:
            if not emprestimo.devolvido and emprestimo.data_devolucao < hoje:
                atrasados.append(emprestimo)
        return atrasados

    def listar_em_atraso(self):
        return self.buscar_emprestimos_atrasados(date.today())

    def proximo_id_emprestimo(self):
        return len(self.emprestimos) + 1
