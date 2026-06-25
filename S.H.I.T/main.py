from empresa import Empresa


def menu():
    empresa = Empresa()

    while True:
        print("\nSISTEMA DE HELP DESK")
        print("1. Cadastrar cliente")
        print("2. Total de clientes")
        print("3. Enviar técnico")
        print("4. Pesquisar chamado")
        print("5. Alterar status do chamado")
        print("6. Excluir chamado")
        print("7. Relatório financeiro")
        print("0. Sair")

        opcao = input("Escolha uma opção: ")

        match opcao:
            case "1":
                empresa.cadastrar_clientes()
            case "2":
                empresa.listar_clientes()
            case "3":
                empresa.lancar_tecnico()
            case "4":
                empresa.pesquisar_chamado()
            case "5":
                empresa.alterar_status()
            case "6":
                empresa.excluir_chamado()
            case "7":
                empresa.relatorio_financeiro()
            case "0":
                print("\nSistema Encerrado.")
                break
            case _:
                print("\nOpção inválida.")


menu()
