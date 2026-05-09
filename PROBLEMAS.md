# PROBLEMAS DO SISTEMA LEGADO — REVISÃO COM VOCABULÁRIO TÉCNICO

## Revisão com vocabulário técnico

### 1. Classe Sistema centraliza múltiplas responsabilidades
O sistema apresenta baixa coesão, pois mistura regras de negócio, persistência, interface CLI e notificação no mesmo módulo, violando o SRP.

### 2. Uso de variáveis globais
Há alto acoplamento por estado compartilhado, dificultando testes e manutenção.

### 3. Notificação misturada com lógica de negócio
Existe ausência de separação de responsabilidades, tornando mudanças de comunicação dependentes da lógica principal.

### 4. Dados em dicionários
Há ausência de ocultamento de informação e falta de contrato tipado.

### 5. Interface diretamente ligada à regra
Existe acoplamento excessivo entre apresentação e aplicação.
