# Notificador: responsável pela comunicação com o usuário.
from servicos.interfaces import INotificador


class Notificador(INotificador):

    # Notificação de registro de empréstimo
    def notificar_emprestimo(self, email: str, data_devolucao):
        print(
            f"[EMAIL] Empréstimo registrado para {email}. "
            f"Data prevista para devolução: {data_devolucao}"
        )

    # Notificação de devolução concluída
    def notificar_devolucao(self, email: str, multa: float = 0.0):
        print(
            f"[EMAIL] Devolução registrada com sucesso para {email}"
        )

    # Notifica atraso com multa
    def notificar_atraso(self, email: str):
        print(
            f"[EMAIL] Atenção {email}: empréstimo em atraso."
        )
