# Emprestimo: contrato de empréstimo.
from dataclasses import dataclass
from datetime import date

@dataclass
class Emprestimo:
    id: int
    equipamento_id: int
    nome_usuario: str
    email_usuario: str
    data_emprestimo: date
    data_devolucao: date
    devolvido: bool = False
