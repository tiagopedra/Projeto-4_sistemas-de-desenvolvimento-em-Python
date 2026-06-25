from bancodados import criar_banco
from sistema import Sistema

def menu():
    criar_banco()
    sistema=Sistema()

    while True:
        print("\n============================================")
        print("🛍️  SISTEMA DE VENDAS E PEDIDOS | ORDERFLOW")
        print("============================================")
        print("1 - 🛒 Adicionar ao carrinho")
        print("2 - 🗑️  Remover item do carrinho")
        print("3 - 💳 Finalizar pedido")
        print("4 - 🧾 Ver pedido")
        print("5 - 🚚 Atualizar status")
        print("6 - 💵 Relatório financeiro")
        print("0 - ❌ Sair")

        opcao=input("\nEscolha: ")

        if opcao=="1":
            sistema.adicionar_carrinho()
        elif opcao=="2":
            sistema.remover_item_carrinho()
        elif opcao=="3":
            sistema.finalizar_pedido()
        elif opcao=="4":
            sistema.pedido.exibir_pedido()
        elif opcao=="5":
            sistema.atualizar_status()
        elif opcao=="6":
            sistema.relatorio_financeiro()
        elif opcao=="0":
            print("\nSistema encerrado.")
            break
        else:
            print("\nOpção inválida.")

menu()