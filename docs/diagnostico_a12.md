# Diagnóstico de Code Smells — Aula 12

## 1. Primitive Obsession

**Arquivo:** `servicos/servico_emprestimo.py`

**Smell:** Primitive Obsession

**Situação:** identificado e corrigido.

O evento utilizado pelo Observer era representado por um `dict`, fazendo com que os atributos fossem acessados por chaves. Isso dificultava a compreensão do contrato do evento e permitia erros de chave em tempo de execução.

**Refactoring aplicado:** Replace Primitive with Object.

O `dict` foi substituído pela classe `Evento`, implementada com `@dataclass`.

Agora os dados são acessados por atributos:

```python
evento.tipo
evento.email
evento.data
evento.multa
2. Mysterious Name

Arquivo: tests/conftest.py

Smell: Mysterious Name

Situação: corrigido.

O parâmetro equip_id possuía uma abreviação que não expressava completamente sua finalidade.

Refactoring aplicado: Rename.

O nome foi alterado para:

equipamento_id

A alteração torna o código mais legível e deixa explícito que o valor representa o identificador de um equipamento.

3. Duplicated Code

Arquivo: servicos/notificador_email.py

Smell: Duplicated Code

Situação: identificado.

Os diferentes tipos de notificação possuem estruturas semelhantes e trabalham com os mesmos dados do evento.

A utilização da classe Evento centraliza a representação das informações e permite que a notificação trabalhe sobre uma estrutura comum.

Refactoring aplicado: Replace Primitive with Object.

A representação única do evento reduz a duplicação da estrutura de dados utilizada pelas notificações.

4. Comments

Arquivo: servicos/servico_emprestimo.py

Smell: Comments

Situação: analisado.

Comentários que apenas explicam operações já evidentes podem indicar que o código não expressa claramente sua intenção.

A criação da função _imprimir_linha_atraso() melhora a comunicação da intenção do código pelo próprio nome da função.

Refactoring aplicado: Extract Function.

A impressão dos dados de atraso foi separada da lógica principal de listar_atrasados().

5. Feature Envy

Arquivo: servicos/servico_emprestimo.py

Smell: Feature Envy

Situação: analisado.

O serviço precisa consultar informações do equipamento para calcular a multa. A regra de cálculo permanece concentrada no próprio equipamento e na estratégia de multa.

O cálculo é realizado por:

equipamento.calcular_multa(dias_atraso)

Dessa forma, o serviço coordena a operação enquanto a regra de cálculo permanece encapsulada no objeto responsável.

Decisão: manter a delegação existente.

6. Data Class — falso positivo

Arquivo: modelos/equipamento.py

Smell aparente: Data Class

Situação: falso positivo — não refatorar.

As classes Notebook, Projetor e Tablet possuem estrutura simples e podem aparentar um Data Class Smell.

Entretanto, elas representam tipos diferentes de equipamento utilizados pelo sistema. Essas classes fazem parte da estrutura criada anteriormente com Strategy e Factory.

Aplicar Inline Class poderia remover uma distinção importante do domínio e prejudicar a estrutura desenvolvida na Aula 11.

Portanto, a decisão foi manter as classes e registrar o caso como falso positivo.

Conclusão

A principal melhoria realizada na Aula 12 foi substituir a representação do evento baseada em dict por uma @dataclass Evento.

Também foram realizados Rename e Extract Function, mantendo o comportamento observável do sistema.

Os testes automatizados foram utilizados como mecanismo de segurança durante as alterações.

Ao final da implementação, a suíte apresentou:

22 passed

O pipeline do GitHub Actions também apresentou execução verde, confirmando que as alterações atuais estão passando pela suíte automatizada.


### Depois de colar

**Pare. Não coloque mais nada dentro do arquivo.**

Vá até **Commit changes**.

No campo **Commit message**, coloque:

```text
docs: completa diagnostico de code smells da Aula 12
