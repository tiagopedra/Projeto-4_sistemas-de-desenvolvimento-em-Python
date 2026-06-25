class Estudante:

    def __init__(self, matricula, nome, email, nota1, nota2):
        self.matricula = matricula
        self.nome = nome
        self.email = email
        self.nota1 = nota1
        self.nota2 = nota2
        self.media = self.calcular_media()
        self.status = self.calcular_status()
       
    def calcular_media(self):
        self.media = (self.nota1 + self.nota2) / 2
        return self.media
    
    def calcular_status(self):
        if self.media >= 7:
            return "Aprovado!"
        else:
            return "Reprovado!"

    def exibir_dados(self):
        print("\nDADOS DOS ESTUDANTES: ")
        print("\nMatrícula: ", self.matricula)
        print("Nome: ", self.nome)
        print("Email: ", self.email)

    def exibir_dados_faculdade(self):
        print("\nDADOS DOS ESTUDANTES: ")
        print("\nMatrícula: ", self.matricula)
        print("Nome: ", self.nome)
        print("Email: ", self.email)
        print("Nota 1: ", self.nota1)
        print("Nota 2: ", self.nota2)
        print(f"Média: {self.media:.1f}")
        print(f"\nStatus: {self.status}\n")
