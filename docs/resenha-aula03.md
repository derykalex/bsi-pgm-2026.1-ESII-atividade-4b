# Resenha Aula 3 — Modelos UML e Design de Componentes

**Aluno:** Alex da Silva Oliveira  
**Data:** 2026.1  

---

## Questão 1 — Modelos UML como ferramentas de modelagem

### (a) Estrutura × comportamento
Segundo Valente, modelos UML representam abstrações orientadas a objetivos específicos. O diagrama de classes destaca a estrutura estática do sistema, apresentando classes, atributos, métodos e relacionamentos, mas não mostra a dinâmica temporal. Já o diagrama de sequência enfatiza comportamento, revelando interações entre objetos ao longo do tempo. Essas representações são complementares porque uma evidencia organização estrutural e a outra explicita execução operacional.

### (b) Consequência prática
Diagramas de classes ajudam a decidir responsabilidades, fronteiras e organização arquitetural. Diagramas de sequência apoiam decisões sobre fluxo de execução, colaboração entre objetos e métodos necessários para realizar casos de uso.

### (c) Aplicação ao UC01
No UC01 (Registrar Empréstimo), o diagrama de sequência revela quais objetos interagem, em que ordem e quais métodos precisam existir, como busca de equipamento, validação de disponibilidade, salvamento de empréstimo e notificação ao usuário.

---

## Questão 2 — Arquitetura, design e os princípios de decomposição

### (a) Definições
Coesão representa o foco interno de um módulo em responsabilidades relacionadas. Acoplamento é o grau de dependência entre módulos distintos. Ocultamento de informação consiste em proteger detalhes internos, expondo apenas interfaces necessárias.

### (b) Relações entre os princípios
Ocultamento reduz dependência estrutural e favorece baixo acoplamento. Alta coesão fortalece clareza e previsibilidade. O equilíbrio entre esses princípios orienta módulos especializados sem dependência excessiva.

### (c) Aplicação ao projeto v2.0
No projeto v2.0, `modelos/` concentra entidades de domínio, `servicos/` concentra regras de negócio, `repositorios/` centraliza persistência e `main.py` realiza interação com usuário. Essa separação aplica SRP e melhora manutenção.

---

## Questão 3 — Crítica fundamentada à documentação do sistema legado

### (a) Pontos frágeis
A documentação do sistema legado revela baixa coesão ao centralizar múltiplas responsabilidades em uma única estrutura e alto acoplamento devido ao uso de estado global e dependências misturadas.

### (b) Ponto forte
A identificação explícita de dívida técnica demonstra maturidade crítica, pois reconhece limitações estruturais e orienta evolução planejada.

### (c) Síntese
A transparência sobre dívida técnica indica consciência de qualidade de software e estabelece postura de melhoria incremental, alinhada à evolução da v2.0.

---

## Questão 4 — Tipos como contratos: dicionários × classes

### (a) Prevenção de erros
Classes reduzem falhas por nomes incorretos de campos, ausência de atributos e inconsistências de tipos, oferecendo contratos mais claros.

### (b) Capacidade de evolução
Classes permitem incorporar métodos e comportamento sem alterar consumidores externos, promovendo extensibilidade.

### (c) Comunicação do design
Um tipo como `Equipamento` comunica papel semântico e intenção arquitetural, enquanto `dict` oferece apenas estrutura genérica, reduzindo clareza de projeto.
