# Production Readiness Checklist

## 1. Pipeline e qualidade

| Item | Status | Esforço | Prioridade | Observação |
|---|---|---|---|---|
| Lint executado automaticamente a cada push | ✅ OK | feito | alta | Ruff está configurado no pipeline e executa a verificação do código. |
| Testes automatizados executados no CI | ✅ OK | feito | alta | O GitHub Actions executa a suíte de testes automaticamente. |
| Gate de cobertura mínima de 80% | ⚠️ PARCIAL | 2–4 horas | alta | O pipeline possui o comando de cobertura com limiar de 80%, mas é necessário acompanhar e fechar eventuais lacunas de cobertura. |

## 2. Containerização

| Item | Status | Esforço | Prioridade | Observação |
|---|---|---|---|---|
| Receita de build com Dockerfile | ❌ FALTA | 4–8 horas | média | O projeto ainda não possui uma receita de containerização documentada. |
| Ambiente reprodutível por container | ❌ FALTA | 4–8 horas | média | É necessário definir imagem, dependências e comando de inicialização. |
| Execução do container sem root | ❌ FALTA | 2–4 horas | baixa | Ainda não existe configuração de usuário não privilegiado para o container. |

## 3. Persistência

| Item | Status | Esforço | Prioridade | Observação |
|---|---|---|---|---|
| Empréstimos sobrevivem ao encerramento do programa | ❌ FALTA | 1–2 dias | alta | Os dados do sistema são mantidos em memória e podem ser perdidos quando o processo termina. |
| Persistência dos equipamentos | ❌ FALTA | 1–2 dias | alta | É necessário utilizar armazenamento persistente para manter os dados entre execuções. |
| Backup dos dados | ❌ FALTA | 1 dia | média | Ainda é necessário definir uma estratégia de backup e recuperação dos dados. |

## 4. Segurança

| Item | Status | Esforço | Prioridade | Observação |
|---|---|---|---|---|
| Dependências de desenvolvimento versionadas | ✅ OK | feito | alta | As dependências de desenvolvimento estão registradas no requirements-dev.txt. |
| Entradas do usuário validadas | ⚠️ PARCIAL | 4–8 horas | alta | A interface possui controles de entrada, mas a validação deve ser revisada em todas as operações. |
| Auditoria de dependências e vulnerabilidades | ❌ FALTA | 4–8 horas | média | Ainda é necessário estabelecer uma verificação sistemática de vulnerabilidades das dependências. |

## 5. Observabilidade

| Item | Status | Esforço | Prioridade | Observação |
|---|---|---|---|---|
| Logs com nível definido | ⚠️ PARCIAL | 4–8 horas | média | Existem mecanismos de comunicação e mensagens, mas é necessário consolidar uma estratégia de logging. |
| Métricas de execução do sistema | ❌ FALTA | 1–2 dias | média | Ainda não existem métricas estruturadas para acompanhar o comportamento da aplicação. |
| Investigação de falhas anteriores | ⚠️ PARCIAL | 4–8 horas | média | O GitHub Actions fornece histórico das execuções, mas a aplicação precisa de logs persistentes para investigação operacional. |

## 6. Deployment

| Item | Status | Esforço | Prioridade | Observação |
|---|---|---|---|---|
| Processo definido para disponibilizar uma nova versão | ⚠️ PARCIAL | 4–8 horas | alta | O CI já valida alterações, mas ainda é necessário definir o fluxo completo de entrega da aplicação. |
| Deploy automatizado | ❌ FALTA | 1–2 dias | média | O pipeline atual está concentrado em qualidade, testes e cobertura. |
| Plano de rollback | ❌ FALTA | 4–8 horas | alta | É necessário definir como retornar rapidamente para uma versão anterior caso uma implantação apresente problemas. |

## Síntese executiva

Para tornar o sistema mais próximo de um estado production-ready, os três primeiros pontos a serem atacados devem ser: persistência, cobertura/testes e deployment. A persistência deve vir primeiro porque atualmente os dados dos empréstimos dependem da execução do processo. Se a aplicação for encerrada, os dados mantidos apenas em memória podem ser perdidos. Portanto, antes de ampliar a entrega do sistema, é importante garantir que os dados sobrevivam às reinicializações.

Em segundo lugar, deve-se consolidar a qualidade automatizada, mantendo o lint e os testes no pipeline e garantindo o gate de cobertura mínima de 80%. Essa etapa reduz o risco de regressões antes que novas versões avancem no processo de entrega. O histórico desta atividade demonstra esse princípio: uma alteração proposital fez o pipeline falhar e a correção fez a execução voltar ao estado verde.

Em terceiro lugar, deve-se estruturar o deployment e definir um plano de rollback. A entrega automatizada depende de uma aplicação suficientemente estável e de dados persistentes. Por isso, faz sentido atacar primeiro os itens que reduzem risco e destravam os demais.

A containerização pode ser desenvolvida em seguida, pois ajudará a tornar o ambiente mais reprodutível. Já métricas mais avançadas de observabilidade podem esperar, desde que existam mecanismos mínimos para investigação de falhas. Essa ordem considera risco, esforço e dependências entre as melhorias, evitando investir primeiro em funcionalidades que não resolvem os principais riscos operacionais.
