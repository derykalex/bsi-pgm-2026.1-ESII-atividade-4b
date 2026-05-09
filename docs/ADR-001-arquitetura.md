# ADR-001 — Decisão Arquitetural da v2.0

## Contexto
O sistema legado `emprestimos.py` foi desenvolvido em arquivo único, concentrando regras de negócio, armazenamento de dados, notificações e interface CLI em um único módulo. Essa estrutura gera baixa coesão, alto acoplamento e dificulta manutenção, testes e evolução do sistema. Para atender RNF03 (facilidade de extensão) e RNF04 (testabilidade sem dependência de estado global), tornou-se necessária uma reorganização estrutural.

## Opções consideradas

### Arquivo único
Apresenta simplicidade inicial, porém mantém responsabilidades misturadas, dificulta manutenção e amplia dependências internas.

### MVC
Fornece boa separação estrutural, mas adiciona complexidade superior à necessidade de um sistema CLI acadêmico.

### Arquitetura em camadas
Oferece separação clara entre domínio, regras de negócio, persistência e interface, equilibrando organização, simplicidade e facilidade de manutenção.

## Decisão
Adotar arquitetura em camadas com a seguinte estrutura:

- `modelos/` → Representação do domínio e contratos tipados (`Equipamento`, `Emprestimo`)
- `servicos/` → Regras de negócio e notificações (`ServicoEmprestimo`, `Notificador`)
- `repositorios/` → Armazenamento, busca e atualização de dados
- `main.py` → Interface CLI e interação com usuário

## Consequências
A nova estrutura melhora coesão, reduz acoplamento, favorece SRP, facilita testes e cria base para futuras melhorias com OCP e DIP. O sistema torna-se mais modular, compreensível e sustentável.
