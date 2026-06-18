from datetime import date, timedelta
from modelos.emprestimo import Emprestimo
from repositorios.interfaces import IRepositorioEmprestimo
from servicos.observer import Subject

class ServicoEmprestimo(Subject):
    def __init__(self, repositorio: IRepositorioEmprestimo):
        super().__init__()
        self.repositorio = repositorio

    def registrar(self, equip_id: int, nome: str, email: str, dias: int):
        equipamento = self.repositorio.buscar_equipamento(equip_id)
        if not equipamento or not equipamento.disponivel:
            return False

        emprestimo = Emprestimo(
            id=self.repositorio.proximo_id_emprestimo(),
            equipamento_id=equip_id,
            usuario_nome=nome,
            usuario_email=email,
            data_emprestimo=date.today(),
            data_devolucao=date.today() + timedelta(days=dias)
        )

        self.repositorio.salvar_emprestimo(emprestimo)
        self.repositorio.marcar_indisponivel(equip_id)

        self.notificar({"tipo": "emprestimo", "email": email, "data": emprestimo.data_devolucao})
        return True

    def registrar_devolucao(self, emprestimo_id: int):
        emprestimo = self.repositorio.buscar_emprestimo(emprestimo_id)
        if not emprestimo or emprestimo.devolvido:
            return False

        hoje = date.today()
        multa = 0.0
        if hoje > emprestimo.data_devolucao:
            dias_atraso = (hoje - emprestimo.data_devolucao).days
            equipamento = self.repositorio.buscar_equipamento(emprestimo.equipamento_id)
            if equipamento:
                multa = equipamento.calcular_multa(dias_atraso)

        self.repositorio.marcar_devolvido(emprestimo_id)
        self.repositorio.marcar_disponivel(emprestimo.equipamento_id)

        self.notificar({"tipo": "devolucao", "email": emprestimo.usuario_email, "multa": multa})
        return True

    def listar_atrasados(self):
        atrasados = self.repositorio.listar_em_atraso()
        if not atrasados:
            print("Nenhum empréstimo em atraso.")
            return
        print("\n=== EMPRÉSTIMOS EM ATRASO ===")
        for emprestimo in atrasados:
            dias_atraso = (date.today() - emprestimo.data_devolucao).days
            equipamento = self.repositorio.buscar_equipamento(emprestimo.equipamento_id)
            multa = equipamento.calcular_multa(dias_atraso) if equipamento else 0.0
            print(f"ID: {emprestimo.id} | Usuário: {emprestimo.usuario_nome} | Email: {emprestimo.usuario_email} | Multa: R${multa:.2f}")
            self.notificar({"tipo": "atraso", "email": emprestimo.usuario_email})
        return atrasados
