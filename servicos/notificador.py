# Notificador: responsável por comunicação com usuário.
class Notificador:

    # Notifica registro de empréstimo
    def notificar_emprestimo(self, email: str, data_devolucao):
        print(
            f"[EMAIL] Empréstimo registrado para {email}. "
            f"Data prevista para devolução: {data_devolucao}"
        )

    # Notifica devolução concluída
    def notificar_devolucao(self, email: str):
        print(
            f"[EMAIL] Devolução registrada com sucesso para {email}."
        )

    # Notifica atraso com multa
    def notificar_atraso(self, email: str, multa: float):
        print(
            f"[EMAIL] Atenção {email}: empréstimo em atraso. "
            f"Multa acumulada: R$ {multa:.2f}"
        )
