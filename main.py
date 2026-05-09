# main.py: ponto de entrada principal do sistema.
from servicos.servico_emprestimo import ServicoEmprestimo


def exibir_menu():
    print("\n=== SISTEMA DE EMPRÉSTIMOS ===")
    print("1. Registrar Empréstimo")
    print("2. Registrar Devolução")
    print("3. Listar Empréstimos em Atraso")
    print("4. Sair")


def main():
    servico = ServicoEmprestimo()

    while True:
        exibir_menu()

        opcao = input("Escolha uma opção: ")

        try:
            # UC01
            if opcao == "1":
                equip_id = int(input("ID do equipamento: "))
                nome = input("Nome do usuário: ")
                email = input("Email: ")
                dias = int(input("Quantidade de dias: "))

                sucesso = servico.registrar(
                    equip_id,
                    nome,
                    email,
                    dias
                )

                if sucesso:
                    print("Empréstimo registrado com sucesso.")
                else:
                    print(
                        "Falha no registro: equipamento inexistente ou indisponível."
                    )

            # UC02
            elif opcao == "2":
                emprestimo_id = int(
                    input("ID do empréstimo para devolução: ")
                )

                sucesso = servico.registrar_devolucao(
                    emprestimo_id
                )

                if sucesso:
                    print("Devolução registrada com sucesso.")
                else:
                    print(
                        "Falha na devolução: empréstimo inválido ou já devolvido."
                    )

            # UC03
            elif opcao == "3":
                servico.listar_atrasados()

            # Sair
            elif opcao == "4":
                print("Encerrando sistema...")
                break

            else:
                print("Opção inválida. Tente novamente.")

        except ValueError:
            print(
                "Erro: entrada inválida. Use números onde solicitado."
            )


if __name__ == "__main__":
    main()
