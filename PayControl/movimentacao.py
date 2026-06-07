# Importa a classe Conta, que representa cada conta do sistema
from conta import Conta

# Classe que representa o controle do sistema, responsável pelas operações de movimentação das contas
class Movimentacao:

    # método inicializador recebe o objeto cadastro, que contém as contas e conexão com banco
    def __init__(self, cadastro):
        self.cadastro = cadastro

    # método responsável por registrar o pagamento de uma conta
    def pagar_conta(self):

        # verifica se há contas cadastradas no sistema
        if len(self.cadastro.contas) == 0:
            print("\nNenhuma conta cadastrada.")
            return

        # solicita ao usuário o ID da conta que deseja pagar
        try:
            id_busca = int(input("Digite o ID da conta que deseja pagar: "))
        except ValueError:
            print("ID inválido.")
            return

        # percorre todas as contas cadastradas
        for conta in self.cadastro.contas:

            # verifica se o ID informado corresponde a uma conta existente
            if conta.id == id_busca:

                # impede pagamento duplicado
                if conta.status == "Paga":
                    print("\nEsta conta já está paga.")
                    return

                # exibe os dados da conta encontrada
                print("\nConta encontrada:")
                conta.exibir_dados()

                # solicita confirmação do usuário para efetuar o pagamento
                confirmacao = input("\nConfirmar pagamento desta conta? (s/n): ").lower()

                if confirmacao == "s":

                    # altera o status da conta na memória
                    conta.status = "Paga"

                    # atualiza o status da conta no banco de dados
                    self.cadastro.cursor.execute("""
                    UPDATE contas
                    SET status=?
                    WHERE id=?
                    """, ("Paga", conta.id))

                    # confirma a alteração no banco
                    self.cadastro.conn.commit()

                    print("\nConta marcada como paga com sucesso.")
                else:
                    print("\nOperação cancelada.")

                return

        # caso nenhum ID seja encontrado
        print("\nConta não encontrada.")

    # método responsável por atualizar os dados de uma conta
    def atualizar_contas(self):

        # verifica se existem contas cadastradas
        if len(self.cadastro.contas) == 0:
            print("\nNenhuma conta cadastrada.")
            return

        # solicita o ID da conta que será atualizada
        try:
            id_busca = int(input("Digite o ID da conta: "))
        except ValueError:
            print("ID inválido.")
            return

        # percorre todas as contas para encontrar a correspondente
        for conta in self.cadastro.contas:

            # verifica se o ID corresponde
            if conta.id == id_busca:

                # exibe a conta encontrada
                print("\nConta encontrada\n:")
                conta.exibir_dados()

                # apresenta opções de atualização
                print("\n#### O que deseja atualizar na Conta? ####")
                print("[1]. Nome")
                print("[2]. Valor")
                print("[3]. Dia de vencimento")
                print("[4]. Mês de vencimento")
                print("[5]. Ano de Vencimento")
                print("[6]. Status da Conta")

                opcao = int(input("Escolha uma opção: "))

                # atualização do nome
                if opcao == 1:
                    novo_nome = input("Digite o novo nome: ")
                    conta.nome_conta = novo_nome

                # atualização do valor
                elif opcao == 2:
                    while True:
                        try:
                            novo_valor = float(input("Digite o novo valor: "))
                            conta.valor = novo_valor
                            break
                        except ValueError:
                            print("Valor inválido.")

                # atualização do dia
                elif opcao == 3:
                    while True:
                        try:
                            novo_dia = int(input("Digite o novo dia: "))
                            if novo_dia >= 1 and novo_dia <= 31:
                                conta.dia_vencimento = novo_dia
                                break
                            else:
                                print("Dia inválido, digite o dia corretamente.")
                        except ValueError:
                            print("Entrada inválida. Digite o dia corretamente")

                # atualização do mês
                elif opcao == 4:
                    while True:
                        try:
                            novo_mes = int(input("Digite o novo mês: "))
                            if novo_mes >= 1 and novo_mes <= 12:
                                conta.mes_vencimento = novo_mes
                                break
                            else:
                                print("Mês inválido. digite o mês corretamente")
                        except ValueError:
                            print("Entrada inválida. Digite o mês corretamente")
                
                # atualização do ano
                elif opcao == 5:
                    while True:
                        try:
                            novo_ano = int(input("Digite o novo ano: "))
                            if novo_ano >= 2026:
                                conta.ano_vencimento = novo_ano
                                break
                            else:
                                print("Ano inválido. digite o ano corretamente")
                        except ValueError:
                            print("Entrada inválida. Digite o ano corretamente")

                # atualização do status
                elif opcao == 6:
                    while True:
                        try:
                            print("\nEscolha o novo status")
                            print("[1]. Pendente")
                            print("[2]. Atrasada")
                            print("[3]. Paga")
                            
                            novo_status = int(input("Digite a opção: "))
                            
                            if novo_status == 1:
                                conta.status = str("Pendente")
                                break
                            elif novo_status == 2:
                                conta.status = str("Atrasada")
                                break
                            elif novo_status == 3:
                                conta.status = str("Paga")
                            else:
                                print("Opção invalída. Digite uma opção valida")
                        except ValueError:
                            print("Opção invalída. Digite uma opção valida")
                else:
                    print("Opção inválida.")
                    return

                # atualiza as informações da conta no banco de dados
                self.cadastro.cursor.execute("""
                UPDATE contas
                SET nome=?, dia=?, mes=?, ano=?, valor=?, status=?
                WHERE id=?
                """,
                (
                    conta.nome_conta,
                    conta.dia_vencimento,
                    conta.mes_vencimento,
                    conta.ano_vencimento,
                    float(conta.valor),
                    conta.status,
                    conta.id
                ))

                # confirma as alterações
                self.cadastro.conn.commit()

                print("\nConta atualizada com sucesso.")
                return

        # caso a conta não seja encontrada
        print("\nConta não encontrada.")

    # método responsável por excluir uma conta
    def excluir_contas(self):

        # verifica se existem contas cadastradas
        if len(self.cadastro.contas) == 0:
            print("\nNenhuma conta cadastrada.")
            return

        # solicita o ID da conta a ser removida
        try:
            id_busca = int(input("Digite o ID da conta: "))
        except ValueError:
            print("ID inválido.")
            return

        # percorre as contas para encontrar a correspondente
        for conta in self.cadastro.contas:

            if conta.id == id_busca:
                
                # exibe os dados da conta encontrada
                print("\nConta encontrada:")
                conta.exibir_dados()

                # solicita confirmação para exclusão
                confirmacao = input("\nDeseja realmente remover esta conta? (s/n): ").lower()

                if confirmacao == "s":

                    if confirmacao == "s":  # redundância, mas mantida

                        # remove a conta do banco de dados usando o ID
                        self.cadastro.cursor.execute(
                            "DELETE FROM contas WHERE id = ?",
                            (conta.id,)
                        )
                        self.cadastro.conn.commit()

                        # remove a conta da lista em memória
                        self.cadastro.contas.remove(conta)
                        print("\nConta removida com sucesso.")
                else:
                    print("\nRemoção cancelada.")

                return

        # caso não encontre a conta
        print("\nConta não encontrada.")