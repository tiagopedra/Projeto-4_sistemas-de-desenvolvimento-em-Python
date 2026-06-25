class Pedido:

    def __init__(self):
        self.itens=[]
        self.total=0
        self.pagamento=""
        self.status="Aguardando"

        self.nome_cliente=""
        self.cpf=""
        self.endereco=""

    def recalcular_total(self):
        total=0

        for item in self.itens:
            total+=item["produto"].preco*item["quantidade"]

        self.total=total

    def adicionar_item(self,produto,tamanho,quantidade):

        item={
            "produto":produto,
            "tamanho":tamanho,
            "quantidade":quantidade
        }

        self.itens.append(item)
        self.recalcular_total()

    def remover_item(self,indice):

        if indice<0 or indice>=len(self.itens):
            return False

        self.itens.pop(indice)
        self.recalcular_total()
        return True

    def exibir_pedido(self):

        if len(self.itens)==0:
            print("\nCarrinho vazio.")
            return

        print("\n==============================")
        print("🧾 PEDIDO")
        print("==============================")

        print(f"👤 Cliente: {self.nome_cliente}")
        print(f"📄 CPF: {self.cpf}")
        print(f"📍 Endereço: {self.endereco}")

        print("\n🛒 ITENS\n")

        for i,item in enumerate(self.itens,start=1):
            produto=item["produto"]
            tamanho=item["tamanho"]
            quantidade=item["quantidade"]
            subtotal=produto.preco*quantidade

            print(f"{i} - {produto.nome}")
            print(f"  Tamanho: {tamanho}")
            print(f"  Quantidade: {quantidade}")
            print(f"  Subtotal: R${subtotal:.2f}\n")

        print(f"💰 Total: R${self.total:.2f}")
        print(f"💳 Pagamento: {self.pagamento}")
        print(f"📦 Status: {self.status}")
        print("==============================")