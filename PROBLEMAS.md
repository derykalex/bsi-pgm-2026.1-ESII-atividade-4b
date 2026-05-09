# PROBLEMAS DO SISTEMA LEGADO — REVISÃO COM VOCABULÁRIO TÉCNICO

## 1. Baixa coesão
O sistema legado centralizava interface, lógica de negócio, persistência e notificação em um único módulo, violando SRP.

## 2. Alto acoplamento
Dependência de variáveis globais e estado compartilhado dificultava manutenção e testes.

## 3. Ausência de ocultamento de informação
Uso de dicionários expunha estrutura interna e enfraquecia contratos de dados.

## 4. Mistura entre comunicação e negócio
Notificações estavam acopladas à lógica principal.

## 5. Evolução estrutural limitada
A ausência de separação por camadas comprometia escalabilidade e extensibilidade.
