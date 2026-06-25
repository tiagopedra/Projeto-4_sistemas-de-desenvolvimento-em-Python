#CRIA CLASSE ROUPA
class Roupa:

    #MÉTODO CONSTRUTOR
    def __init__(self, nome, codigo, quantidade, valor):
        self.nome = nome
        self.codigo = codigo
        self.quantidade = quantidade
        self.valor = valor

    #MÉTODO PARAR EXIBIR OS ATRIBUTOS DA ROUPA
    def exibir_dados(self):
        print("Peça de roupa:", self.nome)
        print("ID:", self.codigo)
        print("Quantidade:", self.quantidade)
        print(f"Valor: R$", self.valor)



