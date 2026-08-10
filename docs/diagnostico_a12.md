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
