from datetime import date

from modelos.equipamento_factory import EquipamentoFactory
from repositorios.interfaces import IRepositorioEmprestimo


class RepositorioEmprestimo(IRepositorioEmprestimo):
    def __init__(self):
        criar = EquipamentoFactory.criar_equipamento

        self.equipamentos = [
            criar("notebook", 1, "Notebook Dell"),
            criar("projetor", 2, "Projetor Epson"),
            criar("tablet", 3, "Tablet Samsung"),
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

    def listar_em_atraso(self):
        hoje = date.today()

        return [
            emprestimo
            for emprestimo in self.emprestimos
            if not emprestimo.devolvido
            and emprestimo.data_devolucao < hoje
        ]

    def proximo_id_emprestimo(self):
        return len(self.emprestimos) + 1
