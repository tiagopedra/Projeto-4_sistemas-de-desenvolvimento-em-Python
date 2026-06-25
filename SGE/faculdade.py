from database import BancoDeDados


class Faculdade:
    def __init__(self):
        self.banco = BancoDeDados()
        self.estudantes = self.banco.listar_estudantes()

    def validar_nota(self, mensagem):
        while True:
            try:
                nota = float(input(mensagem))

                if 0.0 <= nota <= 10.0:
                    return nota

                print("ERRO: A nota deve estar entre 0.0 e 10.0!")

            except ValueError:
                print("ERRO: Digite um número válido! Use ponto para decimais. Exemplo: 7.5")

    def validar_matricula(self, mensagem):
        while True:
            try:
                matricula = int(input(mensagem))
                return matricula

            except ValueError:
                print("ERRO: A matrícula deve ser um número inteiro!")

    def cadastrar_estudantes(self):
        print("\nCadastro de estudante")

        nome = input("Digite o nome do estudante ou deixe em branco para cancelar: ").strip()

        if not nome:
            print("Cadastro cancelado pelo usuário.")
            return

        email = input("Digite o email do estudante: ").strip()

        nota1 = self.validar_nota("Digite a primeira nota: ")
        nota2 = self.validar_nota("Digite a segunda nota: ")

        matricula = self.banco.cadastrar_estudante(nome, email, nota1, nota2)

        self.estudantes = self.banco.listar_estudantes()

        print(f"\nCadastrado com sucesso! Matrícula: {matricula}.")
        print("A mensalidade ainda não foi cadastrada.")
        print("Para cadastrar, acesse: Menu financeiro > Definir mensalidade.")

    def listar_estudantes(self):
        self.estudantes = self.banco.listar_estudantes()

        if len(self.estudantes) == 0:
            print("\nNenhum estudante cadastrado")
        else:
            print("\nLISTA DOS ESTUDANTES:")

            for estudante in self.estudantes:
                estudante.exibir_dados_faculdade()

    def buscar_estudante(self):
        matricula = self.validar_matricula(
            "Digite a matrícula do estudante a ser buscado: "
        )

        estudante = self.banco.buscar_estudante(matricula)

        if estudante is not None:
            estudante.exibir_dados_faculdade()
        else:
            print("\nEstudante não encontrado!")

    def atualizar_cadastro(self):
        matricula = self.validar_matricula(
            "Digite a matrícula do estudante a ser atualizada: "
        )

        estudante = self.banco.buscar_estudante(matricula)

        if estudante is None:
            print("\nEstudante não encontrado!")
            return

        while True:
            print(f"\nATUALIZANDO ESTUDANTE: {estudante.nome}")
            print("1. Atualizar nome")
            print("2. Atualizar email")
            print("3. Primeira nota")
            print("4. Segunda nota")
            print("0. Concluir e voltar ao menu")

            opcao = input("\nEscolha uma opção: ").strip()

            if opcao == "1":
                estudante.nome = input("Digite o novo nome do estudante: ").strip()
                print("\nNome atualizado com sucesso!")

            elif opcao == "2":
                estudante.email = input("Digite o novo email do estudante: ").strip()
                print("\nEmail atualizado com sucesso!")

            elif opcao == "3":
                estudante.nota1 = self.validar_nota("Digite a nova nota 1: ")
                estudante.calcular_media()
                estudante.status = estudante.calcular_status()
                print("\nPrimeira nota atualizada com sucesso!")

            elif opcao == "4":
                estudante.nota2 = self.validar_nota("Digite a nova nota 2: ")
                estudante.calcular_media()
                estudante.status = estudante.calcular_status()
                print("\nSegunda nota atualizada com sucesso!")

            elif opcao == "0":
                self.banco.atualizar_estudante(
                    estudante.matricula,
                    estudante.nome,
                    estudante.email,
                    estudante.nota1,
                    estudante.nota2
                )

                self.estudantes = self.banco.listar_estudantes()

                print("\nAtualização finalizada e salva no banco!")
                return

            else:
                print("\nOpção inválida! Nenhuma alteração foi feita.")

    def excluir_cadastro(self):
        matricula = self.validar_matricula(
            "Digite a matrícula do estudante a ser excluído: "
        )

        estudante = self.banco.buscar_estudante(matricula)

        if estudante is None:
            print("Estudante não encontrado!")
            return

        self.banco.excluir_estudante(matricula)

        self.estudantes = self.banco.listar_estudantes()

        print("\nCadastro excluído com sucesso!")
