# Diagnóstico de Code Smells - Aula 12

| # | Arquivo:linha                          | Smell (nome técnico)              | Refactoring proposto          | Justificativa |
|---|----------------------------------------|-----------------------------------|-------------------------------|-------------|
| 1 | servicos/notificador_email.py:1        | Primitive Obsession               | Replace Primitive with Object | Evento era dict (sem contrato). Substituído por @dataclass Evento tipada. |
| 2 | servicos/servico_emprestimo.py:55      | Long Method                       | Extract Function              | Método listar_atrasados mistura lógica e impressão → extraído _imprimir_linha_atraso. |
| 3 | servicos/servico_emprestimo.py:30      | Mysterious Name                   | Rename                        | Parâmetros e variáveis renomeados para revelar intenção. |
| 4 | modelos/equipamento.py:15-17           | Data Class (falso positivo)       | Não refatorar                 | Subclasses Notebook/Projetor/Tablet vazias após Strategy. São rótulos de tipo intencionais. Inline Class desfaria OCP + Strategy da Aula 11. |
| 5 | repositorios/repositorio_emprestimo.py:15 | Duplicated Code                | Extract Method                | Lógica de criação de equipamentos duplicada (real + Fake). |
| 6 | servicos/servico_emprestimo.py:65      | Feature Envy (leve)               | Move Function (opcional)      | Cálculo de multa acessa dados de Equipamento. |

**Smell principal resolvido:** Primitive Obsession do evento.
