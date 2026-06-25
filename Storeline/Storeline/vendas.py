#CRIA A CLASSE VENDAS
class Vendas:

    #MÉTODO CONSTRUTOR
    def __init__(self, estoque):
        self.estoque = estoque

    #CRIA O MÉTODO DE SISTEMA DE VENDAS
    def sistema_vendas(self):

        #REPETIÇÃO PARA SEMPRE SER CHAMADO CASO PRECISE
        while True:
            print("\nSISTEMA VENDAS")
            print("-=" * 15)
            print("1. Vender uma roupa")
            print("0. Sair")

            #ESCOLHE A OPÇÃO, E CRIA VÁRIAVEIS ÚTEIS PARA O CÓDIGO
            opcao = input("Escolha uma opção: ")
            encontrado = False
            contador = 0
            falhou = False

            #SE A OPÇÃO FOR 1, EXECUTAR CÓDIGO PARA VENDER UMA ROUPA
            if opcao == "1":

                while True:
                    cpf = input("CPF do cliente (somente números): ").strip()

                    if not cpf.isdigit():
                        print("Erro! Digite apenas números.")
                        continue

                    if len(cpf) != 11:
                        print("Erro! O CPF deve ter exatamente 11 dígitos.")
                        continue

                    break

                self.estoque.cursor.execute(
                    "SELECT * FROM clientes WHERE cpf = ?",
                    (cpf,)
                )

                cliente = self.estoque.cursor.fetchone()

                if cliente:
                    cashback_atual = cliente[3]
                else:
                    cashback_atual = 0

                if not cliente:

                    while True:
                        nome = input("Cliente não encontrado. Digite o nome: ").strip()

                        if len(nome) < 3:
                            print("Erro! O nome deve ter pelo menos 3 caracteres.")
                            continue

                        if nome.isdigit():
                            print("Erro! O nome não pode conter apenas números.")
                            continue

                        break

                    self.estoque.cursor.execute(
                        """
                        INSERT INTO clientes (nome, cpf)
                        VALUES (?, ?)
                        """,
                        (nome, cpf)
                    )

                    self.estoque.conexao.commit()

                    self.estoque.cursor.execute(
                        "SELECT * FROM clientes WHERE cpf = ?",
                        (cpf,)
                    )

                    cliente = self.estoque.cursor.fetchone()

                    print("Cliente cadastrado com sucesso!")

                else:
                    print(f"Cliente encontrado: {cliente[1]}")



                # CRIA REPETIÇÃO, E COM TRY
                while True:
                    try:
                        buscaid = int(input("Qual ID da roupa? "))
                        if buscaid <= 0:
                            print("Erro! O ID deve ser maior que zero.")
                            continue

                        #PROCURA A ROUPA NO BANCO DE DADOS PELO ID INFORMADO
                        self.estoque.cursor.execute(
                            "SELECT * FROM roupas WHERE codigo = ?",
                            (buscaid,)
                        )

                        roupa = self.estoque.cursor.fetchone()
                        if roupa:
                            encontrado = True

                        # SE NÃO FOR ENCONTRADO, APARECE MENSAGEM E CONTADOR ADICIONA +1
                        if not encontrado:
                            print('Erro! Não achamos a roupa, tente novamente.')
                            contador += 1
                            if contador == 3:
                                print('Muitas tentativas inválidas. Voltando ao menu principal.')
                                contador = 0
                                falhou = True
                                break
                        else:
                            break

                    except ValueError:
                        print("Erro! Digite apenas números inteiros.")

                #SE O CONTADOR CHEGAR A 3, VOLTE O CÓDIGO PARA O MENU, IGNORANDO O RESTO
                if falhou:
                    continue

                #ESCOLHE A QUANTIDADE DE PRODUTOS A SER VENDIDO
                while True:
                    try:
                        quantidadevenda = int(input("Qual quantidade de itens? "))
                        if quantidadevenda <= 0:
                            print("Erro! A quantidade deve ser maior que zero.")
                            continue
                        break
                    except ValueError:
                        print("Erro! Digite apenas números inteiros.")

                #UTILIZA WHERE PARA BUSCAR A ROUPA NO BANCO DE DADOS, E CALCULA TOTAL DA VENDA
                self.estoque.cursor.execute(
                    "SELECT * FROM roupas WHERE codigo = ?",
                    (buscaid,)
                )

                roupa = self.estoque.cursor.fetchone()

                if quantidadevenda > roupa[3]:
                    print(
                        f'Atualmente, nossa quantidade desta peça é de {roupa[3]} unidades, tente novamente.'
                    )
                    continue

                total = roupa[4] * quantidadevenda

                if cashback_atual > 0:

                    print(f"Cashback disponível: R${cashback_atual:.2f}")
                    while True:

                        usar = input("Deseja utilizar o cashback? (S/N): ").strip().upper()

                        if usar in ["S", "N"]:
                            break

                        print("Erro! Digite apenas S ou N.")
                    if usar == "S":
                        desconto = min(cashback_atual, total)
                        total -= desconto
                        self.estoque.cursor.execute(
                            """
                            UPDATE clientes
                            SET cashback = cashback - ?
                            WHERE cpf = ?
                            """,
                            (desconto, cpf)
                        )

                        self.estoque.conexao.commit()

                        print(f"Desconto aplicado: R${desconto:.2f}")
                        print(f"Novo total: R${total:.2f}")

                cashback = total * 0.15

                self.estoque.total_vendido += total
                self.estoque.total_pecas_vendidas += quantidadevenda

                print(
                    f'Comprando {quantidadevenda} peças de {roupa[1]}, o valor total fica de R${total:.2f}'
                    .replace(".", ",")
                )

                self.estoque.cursor.execute(
                    """
                    UPDATE clientes
                    SET cashback = cashback + ?
                    WHERE cpf = ?
                    """,
                    (cashback, cpf)
                )

                self.estoque.conexao.commit()

                print(f"Cashback recebido: R${cashback:.2f}")
                self.estoque.cursor.execute(
                    """
                    INSERT INTO vendas
                    (
                        cliente_id,
                        roupa_nome,
                        quantidade,
                        valor_total
                    )
                    VALUES (?, ?, ?, ?)
                    """,
                    (
                        cliente[0],
                        roupa[1],
                        quantidadevenda,
                        total
                    )
                )

                self.estoque.conexao.commit()

                nova_quantidade = roupa[3] - quantidadevenda

                self.estoque.cursor.execute(
                    """
                    UPDATE roupas
                    SET quantidade = ?
                    WHERE codigo = ?
                    """,
                    (nova_quantidade, buscaid)
                )

                self.estoque.conexao.commit()

                if 0 < nova_quantidade <= 10:
                    print(
                        f"\033[33mAVISO: ESTA PEÇA ESTÁ ACABANDO! Restam apenas {nova_quantidade} unidades.\033[m"
                    )

                elif nova_quantidade == 0:
                    print("\033[31mAVISO: ESTA PEÇA ACABOU!\033[m")

                    self.estoque.cursor.execute(
                        "DELETE FROM roupas WHERE codigo = ?",
                        (buscaid,)
                    )

                    self.estoque.conexao.commit()

            # SE A OPÇÃO FOR 0, SAIR DO SISTEMA DE VENDAS, SE NÃO FOR 0 E NEM 1, TENTAR NOVAMENTE
            elif opcao == "0":
                print("\nSISTEMA ENCERRADO.")
                break
            else:
                print(f'Opção inválida, tente novamente.')

    #MOSTRAR HISTÓRICOS DE COMPRAS DOS CLIENTES
    def historico_vendas(self):

        self.estoque.cursor.execute("""
        SELECT
            clientes.nome,
            clientes.cpf,
            vendas.roupa_nome,
            vendas.quantidade,
            vendas.valor_total
        FROM vendas
        INNER JOIN clientes
            ON vendas.cliente_id = clientes.id
        """)

        vendas = self.estoque.cursor.fetchall()

        print("\nHISTÓRICO DE VENDAS")
        print("-=" * 15)

        if len(vendas) == 0:
            print("Nenhuma venda registrada.")
            return

        for venda in vendas:
            print(f"Cliente: {venda[0]}")
            print(f"CPF: {venda[1]}")
            print(f"Produto: {venda[2]}")
            print(f"Quantidade: {venda[3]}")
            print(f"Valor Total: R${venda[4]:.2f}")
            print("-=" * 15)



