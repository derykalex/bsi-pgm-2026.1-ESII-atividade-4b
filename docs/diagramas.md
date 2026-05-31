# Diagramas e Decomposição em Camadas — Atividade 4a / 8

**Aluno:** Alex da Silva Oliveira  
**Disciplina:** Engenharia de Software II  
**Professor:** Fabrício Araújo  

---

## Diagrama de classes — v2.0

```mermaid
classDiagram
    class IRepositorioEmprestimo {
        <<interface>>
        +buscar_equipamento(equip_id)
        +salvar_emprestimo(emprestimo)
        +buscar_emprestimo(emprestimo_id)
        +marcar_indisponivel(equip_id)
        +marcar_disponivel(equip_id)
        +marcar_devolvido(emprestimo_id)
        +listar_em_atraso()
        +proximo_id_emprestimo()
    }

    class INotificador {
        <<interface>>
        +notificar_emprestimo(email, data_devolucao)
        +notificar_devolucao(email, multa)
        +notificar_atraso(email)
    }

    class RepositorioEmprestimo {
        -equipamentos: List[Equipamento]
        -emprestimos: List[Emprestimo]
    }

    class Notificador {
    }

    class ServicoEmprestimo {
        -repositorio: IRepositorioEmprestimo
        -notificador: INotificador
        +registrar(equip_id, nome, email, dias)
        +registrar_devolucao(emprestimo_id)
        +listar_atrasados()
    }

    class Equipamento {
        <<abstract>>
        +id: int
        +nome: str
        +tipo: str
        +disponivel: bool
        +calcular_multa(dias_atraso: int)
    }

    class Notebook {
    }
    class Projetor {
    }
    class Tablet {
    }

    class Emprestimo {
        +id: int
        +equipamento_id: int
        +usuario_nome: str
        +usuario_email: str
        +data_emprestimo: date
        +data_devolucao: date
        +devolvido: bool
    }

    ServicoEmprestimo --> IRepositorioEmprestimo
    ServicoEmprestimo --> INotificador
    RepositorioEmprestimo ..|> IRepositorioEmprestimo
    Notificador ..|> INotificador

    Notebook --|> Equipamento
    Projetor --|> Equipamento
    Tablet --|> Equipamento

    RepositorioEmprestimo o-- Equipamento
    RepositorioEmprestimo o-- Emprestimo
