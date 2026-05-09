# RepositorioEmprestimo: armazenar e recuperar dados.
from modelos.equipamento import Equipamento

class RepositorioEmprestimo:

    def __init__(self):
        self.equipamentos = [
            Equipamento(1, "Notebook Dell", "notebook"),
            Equipamento(2, "Projetor Epson", "projetor"),
            Equipamento(3, "Tablet Samsung", "tablet")
        ]

        self.emprestimos = []

    def buscar_equipamento(self, equip_id: int):
        for equipamento in self.equipamentos:
            if equipamento.id == equip_id:
                return equipamento
        return None

    def salvar_emprestimo(self, emprestimo):
        self.emprestimos.append(emprestimo)

    def marcar_indisponivel(self, equip_id: int):
        equipamento = self.buscar_equipamento(equip_id)
        if equipamento:
            equipamento.disponivel = False

    def buscar_emprestimo(self, emprestimo_id: int):
        for emprestimo in self.emprestimos:
            if emprestimo.id == emprestimo_id:
                return emprestimo
        return None

    def marcar_devolvido(self, emprestimo_id: int):
        emprestimo = self.buscar_emprestimo(emprestimo_id)
        if emprestimo:
            emprestimo.devolvido = True

    def marcar_disponivel(self, equip_id: int):
        equipamento = self.buscar_equipamento(equip_id)
        if equipamento:
            equipamento.disponivel = True

    def buscar_emprestimos_atrasados(self, hoje):
        return [
            emprestimo for emprestimo in self.emprestimos
            if not emprestimo.devolvido and emprestimo.data_devolucao < hoje
        ]
