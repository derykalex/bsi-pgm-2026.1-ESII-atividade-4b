# Reflexões

## Aula 04 — SRP

A decisão de fronteira mais difícil foi separar o Notificador do ServicoEmprestimo. Inicialmente, parecia natural manter a emissão de notificações dentro da própria lógica de empréstimos, pois ambos participam do mesmo fluxo funcional. Contudo, ao aplicar Valente (Cap. 5, princípio de responsabilidade única), tornou-se evidente que regras de comunicação e regras de negócio possuem motivos distintos para mudança.

Se o formato de envio, canal ou mensagem mudasse, isso não deveria obrigar alteração na lógica de empréstimos. Da mesma forma, mudanças na regra de atraso, devolução ou disponibilidade não deveriam impactar o módulo de comunicação. Essa percepção mostrou que manter ambos juntos geraria baixa coesão e múltiplas razões para alteração.

A dificuldade prática esteve em distinguir colaboração entre componentes de responsabilidade estrutural. Mesmo trabalhando juntos, ServicoEmprestimo e Notificador não precisavam ser o mesmo módulo.

A decisão final foi guiada pelo critério de “um único motivo para mudar”, priorizando alta coesão e menor acoplamento. Assim, a separação adotada tornou o sistema mais claro, modular e alinhado ao SRP.


## Aula 05 — OCP

A aplicação do Princípio Aberto/Fechado (OCP) no sistema de empréstimos permitiu substituir estruturas condicionais por polimorfismo, tornando o código mais extensível e manutenível. Ao transformar Equipamento em uma classe abstrata e delegar o cálculo de multa para subclasses como Notebook, Projetor e Tablet, o sistema passou a aceitar novos tipos de equipamento sem necessidade de modificar o Service, reduzindo riscos de regressão e atendendo ao conceito de “aberto para extensão, fechado para modificação”, conforme Valente (Cap. 5).

Essa solução funciona bem quando a principal variabilidade está associada ao tipo de equipamento. Entretanto, caso surjam regras mais complexas — como multas por hora, por dia da semana ou políticas promocionais — a hierarquia atual pode se tornar insuficiente. Nesse cenário, apenas herança pode gerar excesso de subclasses e dificultar manutenção, exigindo padrões mais flexíveis, como Strategy.

Segundo Valente, OCP depende da capacidade de antecipar pontos reais de variação, mas sua aplicação excessiva pode resultar em overengineering. Portanto, a decomposição atual atende adequadamente ao contexto identificado hoje, mas pode precisar evoluir se a variabilidade futura ultrapassar a simples diferenciação por tipo.

## Aula 06 — Verificação de LSP

Todas as subclasses de Equipamento (Notebook, Projetor e Tablet) respeitam o contrato da classe base:

- `calcular_multa(0)` retorna `0.0` ✓
- `calcular_multa(-5)` retorna `0.0` ✓
- Nenhuma lança exceção inesperada.

Portanto, o **LSP está satisfeito**.

## Aula 06 — DIP

O DIP transformou o ServicoEmprestimo de criador em consumidor de suas dependências. Antes ele mesmo instanciava o repositório e o notificador internamente (dependência concreta). Agora ele recebe essas dependências via construtor.

Essa mudança é tanto técnica quanto conceitual. Tecnicamente, passamos os objetos como parâmetros. Conceitualmente, invertemos o controle: quem usa o serviço (main.py) é quem decide qual implementação fornecer. Isso reduz o acoplamento e torna o ServicoEmprestimo mais testável, pois podemos injetar versões falsas (dublês) para testes unitários.

Como afirma Valente (Cap. 5): “O princípio da inversão de dependência diz que módulos de alto nível não devem depender de módulos de baixo nível. Ambos devem depender de abstrações.”

Essa aplicação do DIP cumpre o RNF04 (testabilidade isolada) e prepara o sistema para a aula de testes.

## Aula 08 — Testes

Este teste de integração captura algo que os testes de unidade não capturam: a integração real entre as camadas (ServicoEmprestimo, RepositorioEmprestimo e Notificador). Ele verifica se as classes concretas trabalham juntas corretamente, incluindo o fluxo completo de registrar um empréstimo e verificar o estado do repositório após a operação. Isso garante que não há problemas de compatibilidade entre as implementações reais.

Por outro lado, o teste de integração **não** captura tão bem falhas isoladas em regras específicas de negócio (como cálculo de multa ou comportamento do Spy), porque tudo roda junto. Os testes unitários com Fake e Spy são melhores para isolar e testar comportamentos individuais com precisão e rapidez. 

A combinação dos dois tipos de teste (unidade + integração) oferece uma boa cobertura: velocidade e isolamento dos unitários com confiança na integração real do sistema.

## Conexão com a próxima aula (Aula 09 — TDD)

A Aula 9, que aborda Test-Driven Development (TDD) segundo Kent Beck e o ciclo **red-green-refactor**, representa uma inversão completa na forma de desenvolver software. Em vez de escrever o código primeiro e depois os testes, o teste se torna o ponto de partida.

Percebo agora que todo o trabalho realizado nesta Atividade 8 foi uma preparação essencial para o TDD. As **interfaces `abc.ABC`** (`IRepositorioEmprestimo` e `INotificador`) criadas fornecem contratos claros e estáveis, enquanto a infraestrutura de **dublês** (`RepositorioFake` e `NotificadorSpy`) permite isolar o comportamento do `ServicoEmprestimo` durante os testes. 

Sem essas abstrações e dublês formais, seria muito mais difícil seguir o ciclo red-green-refactor de forma natural na próxima aula. Essa preparação transforma o TDD de uma prática teórica em algo viável e produtivo no nosso projeto.

Estou ansioso para aplicar o TDD na implementação de novas funcionalidades, confiando na estrutura que construímos até aqui.

