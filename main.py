# main.py: interface CLI.
from servicos.servico_emprestimo import ServicoEmprestimo

def main():
    servico = ServicoEmprestimo()

    while True:
        print("\n=== SISTEMA DE EMPRÉSTIMOS ===")
        print("1. Registrar Empréstimo")
        print("2. Registrar Devolução")
        print("3. Listar Atrasados")
        print("4. Sair")

        opcao = input("Escolha: ")

        if opcao == "1":
            equip_id = int(input("ID do equipamento: "))
            nome = input("Nome: ")
            email = input("Email: ")
            dias = int(input("Dias: "))

            if servico.registrar(equip_id, nome, email, dias):
                print("Empréstimo registrado com sucesso.")
            else:
                print("Equipamento indisponível.")

        elif opcao == "2":
            emprestimo_id = int(input("ID do empréstimo: "))

            if servico.registrar_devolucao(emprestimo_id):
                print("Devolução registrada.")
            else:
                print("Empréstimo inválido.")

        elif opcao == "3":
            servico.listar_atrasados()

        elif opcao == "4":
            print("Encerrando sistema.")
            break

        else:
            print("Opção inválida.")

if __name__ == "__main__":
    main()
