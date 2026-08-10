from servicos.evento import Evento
from servicos.interfaces import INotificador


class Notificador(INotificador):
    def notificar_emprestimo(self, email, data_devolucao):
        print(
            f"[EMAIL] Empréstimo registrado para {email}. "
            f"Data prevista para devolução: {data_devolucao}"
        )

    def notificar_devolucao(self, email, multa):
        if multa is not None and multa > 0:
            print(
                f"[EMAIL] Devolução registrada para {email}. "
                f"Multa: R${multa:.2f}"
            )
        else:
            print(
                f"[EMAIL] Devolução registrada com sucesso para {email}"
            )

    def notificar_atraso(self, email):
        print(
            f"[EMAIL] Atenção {email}: empréstimo em atraso."
        )

    def notificar(self, evento: Evento):
        if evento.tipo == "emprestimo":
            self.notificar_emprestimo(
                evento.email,
                evento.data,
            )

        elif evento.tipo == "devolucao":
            self.notificar_devolucao(
                evento.email,
                evento.multa,
            )

        elif evento.tipo == "atraso":
            self.notificar_atraso(
                evento.email,
            )
