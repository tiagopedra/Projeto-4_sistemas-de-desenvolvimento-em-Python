# Importa a classe financeiro
from cadastro import Cadastro
from movimentacao import Movimentacao
from exibir import Exibir
from calculo import Calculo


# Função principal do sistema
def menu():

    # Cria os objetos principais do sistema
    cadastro = Cadastro ()
    movimentacao = Movimentacao (cadastro)
    exibir = Exibir (cadastro)
    calculo = Calculo (cadastro)

    # Mantém o sistema em execução e exibe as opções do sistema
    while True:
        try:
            print("\n####################################")
            print("############ PayControl ############")
            print("####################################\n")            
            
            print("[1]. Cadastrar/Atualizar Orçamento")
            print("[2]. Detalhar Orçamento")
            print("[3]. Cadastrar nova conta")
            print("[4]. Listar contas cadastradas")
            print("[5]. Calcular valor a pagar")
            print("[6]. Consultar contas cadastradas")
            print("[7]. Atualizar contas cadastradas")
            print("[8]. Informar pagamento de conta")
            print("[9]. Excluir contas cadastradas")
            print("[0]. Sair")

            opcao = int(input("\nEscolha uma opção: "))

            if opcao == 1:
                cadastro.definir_orcamento()

            elif opcao == 2:
                exibir.relatorio_orcamento_detalhado()
            
            elif opcao == 3:
                cadastro.cadastrar_conta()

            elif opcao == 4:
                exibir.listar_contas()

            elif opcao == 5:
                calculo.total()
        
            elif opcao == 6:
                exibir.pesquisar_contas()

            elif opcao == 7:
                movimentacao.atualizar_contas()

            elif opcao == 8:
                movimentacao.pagar_conta()

            elif opcao == 9:
                movimentacao.excluir_contas()

            elif opcao == 0:
                print("\nSistema encerrado.")
                break

            else:
                print("\nOpção inválida.")
    
        except ValueError:
            print("Digite um valor válido")



menu()