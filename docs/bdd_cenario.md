# Funcionalidade: Desconto por Devolução Antecipada

Cenário: devolução com antecedência gera desconto
Dado um livro emprestado
E o usuário devolve o livro 3 dias antes do prazo
Quando o desconto é calculado com valor diário de R$ 5,00
Então o desconto deve ser R$ 15,00

Cenário: devolução sem adiantamento não gera desconto
Dado um livro emprestado
E o usuário devolve o livro no prazo ou com atraso
Quando o desconto é calculado
Então o desconto deve ser R$ 0,00
