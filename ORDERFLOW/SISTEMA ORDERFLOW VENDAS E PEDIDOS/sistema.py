import sqlite3
from produto import Produto
from pedido import Pedido
from catalogo import mostrar_categorias, categoria_por_opcao

class Sistema:

    def __init__(self):
        self.produtos=[]
        self.pedido=Pedido()
        self.carregar_produtos()
    def carregar_produtos(self):
        conexao=sqlite3.connect("loja_vendas.db")
        cursor=conexao.cursor()
        cursor.execute("SELECT * FROM produtos")
        dados=cursor.fetchall()

        for item in dados:
            produto=Produto(
                item[0],
                item[1],
                item[2],
                item[3]
            )
            self.produtos.append(produto)
        conexao.close()

    def produtos_da_categoria(self,categoria):
        encontrados=[]

        for produto in self.produtos:
            if produto.categoria==categoria:
                encontrados.append(produto)

        return encontrados

    def escolher_categoria(self):
        while True:
            mostrar_categorias()
            print("0 - Voltar")
            opcao=input("\nEscolha uma categoria: ")

            if opcao=="0":
                return None
            categoria=categoria_por_opcao(opcao)

            if categoria is None:
                print("Categoria inválida.")
                continue

            return categoria

    def mostrar_produtos_categoria(self,categoria):
        encontrados=self.produtos_da_categoria(categoria)

        print(f"\n========== {categoria.upper()} ==========\n")

        if len(encontrados)==0:
            print("Nenhum produto encontrado.")
            return []

        for produto in encontrados:
            produto.exibir()

        return encontrados

    def escolher_tamanho(self,produto):
        if produto.categoria=="Calçados":
            tamanho=input("Digite o número do calçado (34 a 44): ")

            if tamanho.isdigit():
                tamanho=int(tamanho)

                if tamanho>=34 and tamanho<=44:
                    return str(tamanho)

            print("Tamanho inválido.")
            return ""

        print("\nTamanhos disponíveis: P | M | G | GG")
        tamanho=input("Escolha o tamanho: ").upper().strip()

        if tamanho=="P" or tamanho=="M" or tamanho=="G" or tamanho=="GG":
            return tamanho

        print("Tamanho inválido.")
        return ""

    def escolher_quantidade(self):
        quantidade=input("Quantidade: ").strip()

        if quantidade.isdigit():
            quantidade=int(quantidade)

            if quantidade>0:
                return quantidade

        print("Quantidade inválida.")
        return 0

    def adicionar_carrinho(self):
        if self.pedido.status!="Aguardando":
            print("\nPedido já finalizado.")
            return

        while True:
            categoria=self.escolher_categoria()

            if categoria is None:
                return

            produtos_categoria=self.mostrar_produtos_categoria(categoria)

            if len(produtos_categoria)==0:
                voltar=input("\nDigite qualquer tecla para voltar ou 0 para sair: ")

                if voltar=="0":
                    return

                continue

            print("\n0 - Voltar para categorias")
            escolha=input("\nDigite o código do produto: ")

            if escolha=="0":
                continue

            for produto in produtos_categoria:
                if str(produto.prod)==escolha:
                    tamanho=self.escolher_tamanho(produto)

                    if tamanho=="":
                        return

                    quantidade=self.escolher_quantidade()

                    if quantidade<=0:
                        return

                    self.pedido.adicionar_item(produto,tamanho,quantidade)

                    subtotal=produto.preco*quantidade

                    print(f"\n✅ Produto adicionado ao carrinho.")
                    print(f"Subtotal: R${subtotal:.2f}")
                    return

            print("Produto não encontrado.")

    def remover_item_carrinho(self):
        if self.pedido.status!="Aguardando":
            print("\nPedido já finalizado.")
            return

        if len(self.pedido.itens)==0:
            print("\nCarrinho vazio.")
            return

        self.pedido.exibir_pedido()

        opcao=input("\nDigite o número do item que deseja remover: ")

        if not opcao.isdigit():
            print("Opção inválida.")
            return

        indice=int(opcao)-1

        if self.pedido.remover_item(indice):
            print("\n🗑️ Item removido do carrinho.")
        else:
            print("Item inválido.")

    def finalizar_pedido(self):
        if len(self.pedido.itens)==0:
            print("\nCarrinho vazio.")
            return

        if self.pedido.status!="Aguardando":
            print("\nPedido já finalizado.")
            return

        print("\n==============================")
        print("📋 DADOS DO CLIENTE")
        print("==============================")

        nome=input("Nome: ").strip()
        cpf=input("CPF: ").strip()
        endereco=input("Endereço: ").strip()

        if nome=="" or cpf=="" or endereco=="":
            print("Preencha todos os dados.")
            return

        if not cpf.isdigit() or len(cpf)!=11:
            print("CPF inválido. Digite apenas 11 números.")
            return

        self.pedido.nome_cliente=nome
        self.pedido.cpf=cpf
        self.pedido.endereco=endereco

        print("\n💳 FORMAS DE PAGAMENTO")
        print("1 - Dinheiro")
        print("2 - Cartão")
        print("3 - Pix")

        opcao=input("\nEscolha: ")

        if opcao=="1":
            self.pedido.pagamento="Dinheiro"

        elif opcao=="2":
            self.pedido.pagamento="Cartão"

        elif opcao=="3":
            self.pedido.pagamento="Pix"

        else:
            print("Pagamento inválido.")
            return

        print(f"\n💰 Total da compra: R${self.pedido.total:.2f}")

        confirmar=input("Confirmar pagamento? (s/n): ").lower().strip()

        if confirmar=="s":
            self.pedido.status="Processando"
            print("\n✅ Pagamento aprovado.")
            print("📦 Pedido realizado com sucesso.")

        else:
            print("\nPagamento cancelado.")

    def atualizar_status(self):
        if self.pedido.status=="Aguardando":
            print("\nFinalize o pedido primeiro.")
            return

        if self.pedido.status=="Processando":
            self.pedido.status="Enviado"
            print("\n🚚 Pedido enviado.")

        elif self.pedido.status=="Enviado":
            self.pedido.status="Entregue"
            print("\n📦 Pedido entregue.")

        else:
            print("\nPedido já finalizado.")

    def relatorio_financeiro(self):
        unidades=0

        for item in self.pedido.itens:
            unidades+=item["quantidade"]

        print("\n==============================")
        print("💵 RELATÓRIO FINANCEIRO")
        print("==============================")
        print(f"🛒 Itens no carrinho: {len(self.pedido.itens)}")
        print(f"📦 Unidades vendidas: {unidades}")
        print(f"💰 Valor total: R${self.pedido.total:.2f}")