# Reflexões

## Aula 04 — SRP

A decisão de fronteira mais difícil foi separar o Notificador do ServicoEmprestimo. Inicialmente, parecia natural manter a emissão de notificações dentro da própria lógica de empréstimos, pois ambos participam do mesmo fluxo funcional. Contudo, ao aplicar Valente (Cap. 5, princípio de responsabilidade única), tornou-se evidente que regras de comunicação e regras de negócio possuem motivos distintos para mudança.

Se o formato de envio, canal ou mensagem mudasse, isso não deveria obrigar alteração na lógica de empréstimos. Da mesma forma, mudanças na regra de atraso, devolução ou disponibilidade não deveriam impactar o módulo de comunicação. Essa percepção mostrou que manter ambos juntos geraria baixa coesão e múltiplas razões para alteração.

A dificuldade prática esteve em distinguir colaboração entre componentes de responsabilidade estrutural. Mesmo trabalhando juntos, ServicoEmprestimo e Notificador não precisavam ser o mesmo módulo.

A decisão final foi guiada pelo critério de “um único motivo para mudar”, priorizando alta coesão e menor acoplamento. Assim, a separação adotada tornou o sistema mais claro, modular e alinhado ao SRP.
