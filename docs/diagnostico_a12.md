# Diagnóstico de Code Smells — Aula 12

## 1. Primitive Obsession

**Arquivo:** `servicos/servico_emprestimo.py:51-55`

**Smell:** Primitive Obsession

**Situação:** identificado e corrigido.

Na versão anterior do sistema, o evento utilizado pelo padrão Observer era representado por um `dict`. Essa representação utilizava chaves como `"tipo"`, `"email"`, `"data"` e `"multa"` sem um contrato explícito.

**Refactoring aplicado:** Replace Primitive with Object.

O `dict` foi substituído pela classe `Evento`, implementada como `@dataclass`. Atualmente o serviço cria eventos tipados:

```python
evento = Evento(
    tipo="emprestimo",
    email=usuario_email,
    data=data_devolucao
)
```

Agora os dados são acessados por atributos, como `evento.tipo`, `evento.email`, `evento.data` e `evento.multa`.

Essa alteração melhora a legibilidade e reduz a possibilidade de erros causados por chaves incorretas.

---

## 2. Mysterious Name

**Arquivo:** `tests/conftest.py:40`

**Smell:** Mysterious Name

**Situação:** identificado e corrigido.

O parâmetro utilizado anteriormente era chamado `equip_id`. A abreviação não deixava completamente explícito que o valor representava o identificador de um equipamento.

**Refactoring aplicado:** Rename.

O parâmetro foi alterado para:

```python
equipamento_id
```

A alteração torna o código mais legível e deixa explícita a finalidade do parâmetro.

---

## 3. Long Method

**Arquivo:** `servicos/servico_emprestimo.py:105-141`

**Smell:** Long Method

**Situação:** identificado e corrigido parcialmente.

O método `listar_atrasados()` concentrava diversas responsabilidades: consultar os empréstimos atrasados, localizar equipamentos, calcular dias de atraso, calcular a multa, imprimir informações e enviar notificações.

**Refactoring aplicado:** Extract Function.

A parte responsável pela impressão das informações de atraso foi extraída para o método:

```python
_imprimir_linha_atraso()
```

A extração separa os detalhes de apresentação do fluxo principal de `listar_atrasados()`.

Com isso, o método principal fica mais organizado e sua intenção é mais fácil de compreender.

---

## 4. Comments

**Arquivo:** `servicos/servico_emprestimo.py:143-153`

**Smell:** Comments

**Situação:** identificado e corrigido.

Comentários que apenas explicam o que o código está fazendo podem indicar que a intenção da operação não está suficientemente clara no próprio código.

Neste caso, a responsabilidade de imprimir os dados do atraso foi extraída para uma função cujo próprio nome explica sua finalidade:

```python
_imprimir_linha_atraso()
```

**Refactoring aplicado:** Extract Function.

A utilização de um nome significativo para a função reduz a necessidade de comentários explicativos sobre uma operação simples.

A própria estrutura do código passa a comunicar sua intenção.

---

## 5. Feature Envy

**Arquivo:** `servicos/servico_emprestimo.py:83-85`

**Smell:** Feature Envy

**Situação:** analisado.

O serviço precisa utilizar informações do equipamento para calcular a multa:

```python
multa = equipamento.calcular_multa(
    dias_atraso
)
```

A regra de cálculo, entretanto, está encapsulada no próprio objeto `Equipamento`, que delega o cálculo para a estratégia de multa.

**Refactoring considerado:** Move Function.

Apesar da possibilidade de mover parte da lógica para outro objeto, a implementação atual mantém o serviço como coordenador do caso de uso e deixa a regra de cálculo encapsulada em `Equipamento` e `MultaStrategy`.

**Decisão:** manter a implementação atual.

Neste caso, a delegação existente mantém uma separação adequada entre a coordenação do empréstimo e a regra de cálculo da multa.

---

## 6. Data Class — falso positivo

**Arquivo:** `modelos/equipamento.py:15-20`

**Smell aparente:** Data Class

**Situação:** falso positivo — não refatorado.

As classes `Notebook`, `Projetor` e `Tablet` possuem estrutura simples e não adicionam métodos próprios:

```python
@dataclass
class Notebook(Equipamento): pass

@dataclass
class Projetor(Equipamento): pass

@dataclass
class Tablet(Equipamento): pass
```

À primeira vista, essas classes podem aparentar um Data Class Smell.

Entretanto, elas representam tipos distintos de equipamento utilizados pelo domínio do sistema. A distinção entre Notebook, Projetor e Tablet é necessária para a estrutura criada anteriormente com Factory e Strategy.

**Refactoring considerado:** Inline Class.

A aplicação de Inline Class eliminaria essas subclasses e removeria uma distinção importante do domínio. Isso também poderia desfazer parte da estrutura desenvolvida nas aulas anteriores.

**Decisão:** não refatorar.

O caso foi registrado como falso positivo porque a estrutura aparentemente simples das classes possui uma finalidade arquitetural no sistema.

---

# Conclusão

O diagnóstico realizado na Aula 12 identificou seis situações relacionadas a Code Smells.

Os principais refactorings realizados foram:

- Replace Primitive with Object;
- Rename;
- Extract Function.

A principal alteração foi substituir a representação do evento baseada em `dict` pela classe `Evento`, implementada com `@dataclass`.

Também foi realizado o Rename de `equip_id` para `equipamento_id` e o Extract Function da impressão dos dados de atraso para `_imprimir_linha_atraso()`.

O possível Data Class nas subclasses `Notebook`, `Projetor` e `Tablet` foi analisado como falso positivo e não foi refatorado, pois essas classes representam tipos distintos do domínio.

Os testes automatizados foram utilizados como rede de segurança durante as alterações. Ao final da implementação, a suíte apresentou:

```text
22 passed
```

O pipeline do GitHub Actions também apresentou execução verde após as alterações, indicando que a suíte automatizada estava passando.
