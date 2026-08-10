from servicos.evento import Evento


class NotificadorEmail:
    def notificar(self, evento: Evento):
        if evento.tipo == "emprestimo":
            print(
                f"[EMAIL] Empréstimo registrado para {evento.email} "
                f"até {evento.data}"
            )

        elif evento.tipo == "devolucao":
            print(
                f"[EMAIL] Devolução registrada para {evento.email}. "
                f"Multa: R${evento.multa:.2f}"
            )

        elif evento.tipo == "atraso":
            print(
                f"[EMAIL] Atraso identificado para {evento.email}. "
                f"Multa: R${evento.multa:.2f}"
            )
