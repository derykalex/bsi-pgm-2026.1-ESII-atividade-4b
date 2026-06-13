# main.py
from app.sistema import SistemaDeEmprestimos


def exibir_menu():
    print("\n=== SISTEMA DE EMPRÉSTIMOS ===")
    print("1. Registrar Empréstimo")
    print("2. Registrar Devolução")
    print("3. Listar Empréstimos em Atraso")
    print("4. Sair")


def main():
    # Facade: uma linha monta tudo
    sistema = SistemaDeEmprestimos()

    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ")

        try:
            if opcao == "1":
                equip_id = int(input("ID do equipamento: "))
                nome = input("Nome do usuário: ")
                email = input("Email: ")
                dias = int(input("Quantidade de dias: "))

                sucesso = sistema.registrar(equip_id, nome, email, dias)
                print("Empréstimo registrado com sucesso." if sucesso else
                      "Falha no registro: equipamento inexistente ou indisponível.")

            elif opcao == "2":
                emprestimo_id = int(input("ID do empréstimo para devolução: "))
                sucesso = sistema.registrar_devolucao(emprestimo_id)
                print("Devolução registrada com sucesso." if sucesso else
                      "Falha na devolução: empréstimo inválido ou já devolvido.")

            elif opcao == "3":
                sistema.listar_atrasados()

            elif opcao == "4":
                print("Encerrando sistema...")
                break

            else:
                print("Opção inválida.")

        except ValueError:
            print("Erro: entrada inválida. Use números onde solicitado.")


if __name__ == "__main__":
    main()
