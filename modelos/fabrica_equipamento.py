# modelos/fabrica_equipamento.py
"""
Simple Factory (Padrão Criacional GoF)
Centraliza a criação de equipamentos.
"""

from modelos.equipamento import Notebook, Projetor, Tablet, Equipamento


class FabricaEquipamento:
    """Simple Factory para criar equipamentos conforme o tipo."""

    @staticmethod
    def criar(tipo: str, id: int, nome: str) -> Equipamento:
        tipo_lower = tipo.lower().strip()

        if tipo_lower in ["notebook", "notebook dell"]:
            return Notebook(id=id, nome=nome, tipo="notebook")
        
        elif tipo_lower in ["projetor", "projetor epson"]:
            return Projetor(id=id, nome=nome, tipo="projetor")
        
        elif tipo_lower in ["tablet", "tablet samsung"]:
            return Tablet(id=id, nome=nome, tipo="tablet")
        
        else:
            raise ValueError(f"Tipo de equipamento desconhecido: {tipo}")
