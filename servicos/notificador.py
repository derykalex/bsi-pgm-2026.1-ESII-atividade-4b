# Notificador: enviar notificações.
class Notificador:

    def notificar_emprestimo(self, email: str, data_devolucao):
        print(f"[EMAIL] Empréstimo registrado para {email}. Devolução até {data_devolucao}.")

    def notificar_devolucao(self, email: str):
        print(f"[EMAIL] Devolução registrada com sucesso para {email}.")

    def notificar_atraso(self, email: str, multa: float):
        print(f"[EMAIL] Empréstimo em atraso para {email}. Multa: R$ {multa:.2f}")
