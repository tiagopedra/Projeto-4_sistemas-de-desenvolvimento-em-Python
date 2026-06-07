#IMPORTA VENDAS, ESTOQUE
from vendas import Vendas
from estoque import Estoque
from cliente import Cliente

#MENU PRINCIPAL
def menu():

    #CRIA OBJETO ESTOQUE
    estoque = Estoque()
    cliente = Cliente(estoque)

    #CRIA VENDAS, E INFORMA PARA TRABALHAR EM CONJUNTO COM O ESTOQUE
    vendas = Vendas(estoque)

    #REPETIÇÃO PARA RODAR O MENU SEMPRE QUE PRECISO
    while True:
        print("-="*15)
        print("       LOJA DE ROUPAS       ")
        print("-="*15)
        print("- 1. Vender uma roupa")
        print("- 2. Roupas no estoque")
        print("- 3. Cadastrar roupa")
        print("- 4. Remover roupa")
        print("- 5. Mostrar relatório de vendas")
        print("- 6. Ver clientes cadastrados")
        print("- 7. Histórico de vendas")
        print("- 0. Sair")

        #ESCOLHA QUAL VOCÊ QUER RODAR
        opcao = input("Escolha uma opção: ").strip()

        # SE A OPÇÃO FOR 1, EXECUTAR O SISTEMA DE VENDAS
        if opcao == "1":
            vendas.sistema_vendas()

        # SE A OPÇÃO FOR 2, EXECUTAR O SISTEMA DE ESTOQUE
        elif opcao == "2":
            estoque.sistema_estoque()

        # SE A OPÇÃO FOR 3, CADASTRAR UMA ROUPA
        elif opcao == "3":
            estoque.cadastrar_roupa()

        #SE A OPÇÃO FOR 4, REMOVER UMA ROUPA
        elif opcao == "4":
            estoque.remover_roupa()

        # SE A OPÇÃO FOR 5, MOSTRAR RELATÓRIO
        elif opcao == "5":
            estoque.relatorio()

        # SE A OPÇÃO FOR 6, EXIBIR CLIENTES CADASTRADOS
        elif opcao == "6":
            cliente.listar_clientes()

        elif opcao == "7":
            vendas.historico_vendas()

        # SE A OPÇÃO FOR 0, SAIR DO SISTEMA
        elif opcao == "0":
            print("\n\033[0;30;41mSISTEMA ENCERRADO!\033[m")
            break

        #SE NÃO FOR NENHUMA OPÇÃO, APARECE A MENSAGEM
        else:
            print("\nOpção inválida.")
menu()