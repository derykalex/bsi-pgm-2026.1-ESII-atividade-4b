from modelos.equipamento import Notebook, Projetor, Tablet
from modelos.multa_strategy import MultaPorDia

class EquipamentoFactory:
    @staticmethod
    def criar_equipamento(tipo: str, id: int, nome: str):
        tipo_lower = tipo.lower().strip()
        if tipo_lower in ["notebook", "notebook dell"]:
            return Notebook(id=id, nome=nome, tipo="notebook", multa=MultaPorDia(10.0))
        elif tipo_lower in ["projetor", "projetor epson"]:
            return Projetor(id=id, nome=nome, tipo="projetor", multa=MultaPorDia(15.0))
        elif tipo_lower in ["tablet", "tablet samsung"]:
            return Tablet(id=id, nome=nome, tipo="tablet", multa=MultaPorDia(10.0))
        else:
            raise ValueError(f"Tipo de equipamento desconhecido: {tipo}")
