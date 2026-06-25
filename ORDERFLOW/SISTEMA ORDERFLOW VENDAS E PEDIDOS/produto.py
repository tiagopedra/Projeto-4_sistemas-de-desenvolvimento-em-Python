class Produto:

    def __init__(self,prod,nome,categoria,preco):
        self.prod=prod
        self.nome=nome
        self.categoria=categoria
        self.preco=preco

    def exibir(self):
        print(f"{self.prod} - {self.nome} | {self.categoria} | R${self.preco:.2f}")