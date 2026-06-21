from servicos.observer import Observer
from servicos.evento import Evento


class NotificadorEmail(Observer):
    def update(self, evento: Evento) -> None:
        """Método do padrão Observer"""
        if evento.tipo == "emprestimo":
            print(f"[EMAIL] {evento.email} — empréstimo até {evento.data}")
        elif evento.tipo == "devolucao":
            print(f"[EMAIL] {evento.email} — multa R${evento.multa or 0:.2f}")
        elif evento.tipo == "atraso":
            print(f"[EMAIL] {evento.email} — você está em atraso!")

    # Compatibilidade com INotificador (chamado pelo ServicoEmprestimo)
    def notificar(self, evento: Evento):
        self.update(evento)

    def notificar_emprestimo(self, email, data_devolucao):
        self.notificar(Evento("emprestimo", email, data=data_devolucao))

    def notificar_devolucao(self, email, multa):
        self.notificar(Evento("devolucao", email, multa=multa))

    def notificar_atraso(self, email):
        self.notificar(Evento("atraso", email))
