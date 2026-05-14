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
