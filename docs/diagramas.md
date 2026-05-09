# Diagramas e Decomposição em Camadas — Atividade 4a

**Aluno:** Alex da Silva Oliveira  
**Disciplina:** Engenharia de Software II  
**Professor:** Fabrício Araújo  

---

# Decomposição em Camadas

## models/Equipamento
Representa a entidade de domínio Equipamento, armazenando seus dados e disponibilidade.

## models/Emprestimo
Representa o contrato de empréstimo, contendo usuário, datas e status.

## services/ServicoEmprestimo
Centraliza regras de negócio de empréstimo, devolução e atrasos.

## services/Notificador
Responsável exclusivamente pelas notificações.

## repositories/RepositorioEmprestimo
Gerencia armazenamento, busca e atualização de dados.

## main.py
Responsável pela interface CLI e interação com usuário.

---

# Diagramas de Sequência

## UC01 — Registrar Empréstimo

```mermaid
sequenceDiagram
 actor Atendente
 participant main as main.py
 participant servico as ServicoEmprestimo
 participant repo as RepositorioEmprestimo
 participant notif as Notificador
 Atendente->>main: informa equip_id, nome, email, dias
 main->>servico: registrar(equip_id, nome, email, dias)
 servico->>repo: buscar_equipamento(equip_id)
 repo-->>servico: Equipamento
 alt equipamento disponível
 servico->>repo: salvar_emprestimo(emprestimo)
 servico->>repo: marcar_indisponivel(equip_id)
 servico->>notif: notificar_emprestimo(email, data_devolucao)
 servico-->>main: True
 else equipamento indisponível
 servico-->>main: False
 end
```
## UC02 — Registrar Devolução

```mermaid
sequenceDiagram
 actor Atendente
 participant main as main.py
 participant servico as ServicoEmprestimo
 participant repo as RepositorioEmprestimo
 participant notif as Notificador
 Atendente->>main: informa emprestimo_id
 main->>servico: registrar_devolucao(emprestimo_id)
 servico->>repo: buscar_emprestimo(emprestimo_id)
 repo-->>servico: Emprestimo
 alt empréstimo ativo
 servico->>repo: marcar_devolvido(emprestimo_id)
 servico->>repo: marcar_disponivel(equip_id)
 servico->>notif: notificar_devolucao(email)
 servico-->>main: True
 else empréstimo inválido
 servico-->>main: False
 end
```

## UC03 — Listar Empréstimos em Atraso

```mermaid
sequenceDiagram
 actor Atendente
 participant main as main.py
 participant servico as ServicoEmprestimo
 participant repo as RepositorioEmprestimo
 Atendente->>main: solicita atrasados
 main->>servico: listar_atrasados()
 servico->>repo: buscar_emprestimos_atrasados()
 repo-->>servico: lista
 alt existem atrasados
 loop para cada empréstimo
 servico-->>main: exibir_atrasado()
 end
 else sem atrasos
 servico-->>main: lista_vazia
 end
```

