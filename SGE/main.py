from faculdade import Faculdade
from financeiro import Financeiro

def menu():

    faculdade = Faculdade()
    financeiro = Financeiro(faculdade)

    while True:
        print("\nSISTEMA DE CONTROLE DE ESTUDANTES")
        print("1. Cadastrar estudantes")
        print("2. Listar estudantes")
        print("3. Buscar estudante")
        print("4. Atualizar cadastro")
        print("5. Excluir cadastro")
        print("6. Menu financeiro")
        print("0. Sair")

        opcao = input("\nEscolha uma opção: ")

        if opcao == "1":
            faculdade.cadastrar_estudantes()

        elif opcao == "2":
            faculdade.listar_estudantes()

        elif opcao == "3":
            faculdade.buscar_estudante()

        elif opcao == "4":
            faculdade.atualizar_cadastro()

        elif opcao == "5":
            faculdade.excluir_cadastro()

        elif opcao == "6":
            financeiro.menu_financeiro()

        elif opcao == "0":
            print("\nSistema encerrado.")
            break
        
        else:
            print("\nOpção inválida")

menu()
