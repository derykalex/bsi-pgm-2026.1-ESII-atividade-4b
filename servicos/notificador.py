from servicos.observadores import Notificador as NotificadorBase


class NotificadorEmail(NotificadorBase):
    """Observer concreto - envio de email"""

    def atualizar(self, evento: str, dados: dict):
        email = dados.get("email")
        if evento == "emprestimo":
            print(f"[EMAIL] Empréstimo registrado para {email}")
        elif evento == "devolucao":
            print(f"[EMAIL] Devolução registrada para {email}")
        elif evento == "atraso":
            print(f"[EMAIL] Atenção {email}: empréstimo em atraso!")
