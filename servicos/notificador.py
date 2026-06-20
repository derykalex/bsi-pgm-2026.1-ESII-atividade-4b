# Notificador: responsável pela comunicação com o usuário.
from servicos.interfaces import INotificador
from servicos.evento import Evento


class Notificador(INotificador):

    def notificar(self, evento: Evento):
        if evento.tipo == "emprestimo":
            print(
                f"[EMAIL] Empréstimo registrado para {evento.email}. "
                f"Data prevista para devolução: {evento.data}"
            )
        elif evento.tipo == "devolucao":
            print(
                f"[EMAIL] Devolução registrada com sucesso para {evento.email}"
            )
        elif evento.tipo == "atraso":
            print(
                f"[EMAIL] Atenção {evento.email}: empréstimo em atraso."
            )
