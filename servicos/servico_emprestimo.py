# ServicoEmprestimo: aplicar regras de negócio.
from datetime import date, timedelta
from modelos.emprestimo import Emprestimo
from repositorios.repositorio_emprestimo import RepositorioEmprestimo
from servicos.notificador import Notificador

class ServicoEmprestimo:

    def __init__(self):
        self.repositorio = RepositorioEmprestimo()
        self.notificador = Notificador()

    def registrar(self, equip_id: int, nome: str, email: str, dias: int):
        equipamento = self.repositorio.buscar_equipamento(equip_id)

        if not equipamento or not equipamento.disponivel:
            return False

        emprestimo = Emprestimo(
            id=len(self.repositorio.emprestimos) + 1,
            equipamento_id=equip_id,
            nome_usuario=nome,
            email_usuario=email,
            data_emprestimo=date.today(),
            data_devolucao=date.today() + timedelta(days=dias)
        )

        self.repositorio.salvar_emprestimo(emprestimo)
        self.repositorio.marcar_indisponivel(equip_id)
        self.notificador.notificar_emprestimo(email, emprestimo.data_devolucao)

        return True

    def registrar_devolucao(self, emprestimo_id: int):
        emprestimo = self.repositorio.buscar_emprestimo(emprestimo_id)

        if not emprestimo or emprestimo.devolvido:
            return False

        self.repositorio.marcar_devolvido(emprestimo_id)
        self.repositorio.marcar_disponivel(emprestimo.equipamento_id)
        self.notificador.notificar_devolucao(emprestimo.email_usuario)

        return True

    def listar_atrasados(self):
        atrasados = self.repositorio.buscar_emprestimos_atrasados(date.today())

        if not atrasados:
            print("Nenhum empréstimo em atraso.")
            return

        for emprestimo in atrasados:
            print(f"ID: {emprestimo.id} | Usuário: {emprestimo.nome_usuario}")
