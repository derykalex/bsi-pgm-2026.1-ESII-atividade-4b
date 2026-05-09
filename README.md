# Atividade 4b — Engenharia de Software II

**Aluno:** Alex da Silva Oliveira  
**Professor:** Fabrício Araújo  
**UFRA — Campus Paragominas**  

---

# Objetivo do Projeto
Refatorar o sistema legado de empréstimos aplicando princípios de Engenharia de Software Moderna:

- Arquitetura em Camadas (ADR-001)
- SRP (Single Responsibility Principle)
- Separação entre interface, regras, persistência e domínio
- Dataclasses como contratos tipados
- Modularização para manutenção e evolução futura

---

# Estrutura do Projeto

## docs/
Documentação acadêmica, diagramas e reflexões.

## modelos/
Entidades do domínio:
- Equipamento
- Emprestimo

## servicos/
Regras de negócio:
- ServicoEmprestimo
- Notificador

## repositorios/
Persistência em memória:
- RepositorioEmprestimo

## main.py
Interface CLI principal.

---

# Casos de Uso Implementados

## UC01 — Registrar Empréstimo
Valida equipamento, registra empréstimo e notifica usuário.

## UC02 — Registrar Devolução
Registra devolução, calcula multa por atraso e notifica usuário.

## UC03 — Listar Empréstimos em Atraso
Exibe empréstimos pendentes fora do prazo.

---

# Execução

```bash
python main.py
