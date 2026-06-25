from datetime import datetime

class Financeiro:
    def __init__(self, faculdade_instancia):
        self.faculdade = faculdade_instancia
        self.banco = faculdade_instancia.banco
        self.taxa_juros = 0.02

    def definir_mensalidade(self):
        print("\nMensalidade do estudante")

        matricula = self.faculdade.validar_matricula("Digite a matrícula do estudante para definir a mensalidade: ")

        estudante_encontrado = None

        
        estudante = self.banco.buscar_estudante(matricula)

        if estudante is None:
            print("ERRO: Estudante não encontrado!")
            return

        estudante.exibir_dados()


        while True:
            try:
                valor = float(input(f"\nDigite o valor da mensalidade para {estudante.nome}: R$ "))

                if valor >= 0:
                    break

                print("ERRO: O valor não pode ser negativo!")

            except ValueError:
                print("ERRO: Digite um número válido para o valor da mensalidade! Use ponto para decimais.")

        while True:
            data = input("Digite a data de vencimento da mensalidade (dd/mm/aaaa): ")

            try:
                vencimento = datetime.strptime(data, "%d/%m/%Y")
                vencimento_formatado = vencimento.strftime("%d/%m/%Y")
                break

            except ValueError:
                print("ERRO: Data inválida! Use o formato dd/mm/aaaa.")

        
        self.banco.definir_mensalidade(
            matricula,
            valor,
            vencimento_formatado)


        print(f"\nMensalidade definida para {estudante.nome}: R$ {valor:.2f}")
        print(f"Data de vencimento: {vencimento_formatado}")

            
    def consultar_mensalidade(self):
        
        print("\nConsulta de mensalidade do estudante")

        matricula = self.faculdade.validar_matricula("Digite a matrícula do estudante para consulta da mensalidade: ")

        dados = self.banco.consultar_financeiro(matricula)

        if dados is None:
            estudante = self.banco.buscar_estudante(matricula)

            if estudante is None:
                print("ERRO: Estudante não encontrado!")
            else:
                print("ERRO: Este estudante ainda não possui mensalidade cadastrada.")

            return

        nome, email, matricula, mensalidade, desconto, vencimento = dados

        resultado = self.calcular_valor_final(mensalidade, desconto, vencimento)
        
        if resultado is None:
            return

        valor_original, desconto, juros, valor_final = resultado

        print("\nStatus da mensalidade do estudante")
        print(f"Nome: {nome}")
        print(f"Email: {email}")
        print(f"Matrícula: {matricula}")
        print(f"Valor original: R$ {valor_original:.2f}")
        print(f"Desconto: R$ {desconto:.2f}")
        print(f"Juros: R$ {juros:.2f}")
        print(f"Valor final: R$ {valor_final:.2f}")
        print(f"Data de vencimento: {vencimento}")


    
    def relatorio_financeiro(self):
        
        print("\nRelatório financeiro dos estudantes")

        dados = self.banco.relatorio_financeiro()

        if len(dados) == 0:
            print("\nNenhuma mensalidade foi cadastrada no sistema.")
            return

        faturamento_original = 0.0
        total_descontos = 0.0
        total_juros = 0.0
        faturamento_final = 0.0

        
        for matricula, nome, email, mensalidade, desconto, vencimento in dados:
            resultado = self.calcular_valor_final(mensalidade, desconto, vencimento)

            if resultado is None:
                continue

            valor_original, desconto, juros, valor_final = resultado

            faturamento_original += valor_original
            total_descontos += desconto
            total_juros += juros
            faturamento_final += valor_final
        
            print("\n--------------------------------")
            print(f"Matrícula: {matricula}")
            print(f"Nome: {nome}")
            print(f"Email: {email}")
            print(f"Mensalidade: R$ {valor_original:.2f}")
            print(f"Desconto: R$ {desconto:.2f}")
            print(f"Juros: R$ {juros:.2f}")
            print(f"Valor final: R$ {valor_final:.2f}")
            print(f"Vencimento: {vencimento}")

        print("\n================================")
        print("RESUMO FINANCEIRO")
        print("================================")
        print(f"Faturamento original: R$ {faturamento_original:.2f}")
        print(f"Total de descontos: R$ {total_descontos:.2f}")
        print(f"Total de juros: R$ {total_juros:.2f}")
        print(f"Faturamento final: R$ {faturamento_final:.2f}")

  

    def aplicar_desconto(self):
        
        print("\nAplicar desconto na mensalidade")

        matricula = self.faculdade.validar_matricula("Digite a matrícula do estudante para aplicar desconto: " )

        dados = self.banco.consultar_financeiro(matricula)

        if dados is None:
            estudante = self.banco.buscar_estudante(matricula)

            if estudante is None:
                print("ERRO: Estudante não encontrado!")
            else:
                print("ERRO: Este estudante ainda não possui mensalidade cadastrada.")

            return

         
        nome, email, matricula, mensalidade, desconto_atual, vencimento = dados

        print(f"\nEstudante: {nome}")
        print(f"Mensalidade atual: R$ {mensalidade:.2f}")
        print(f"Desconto atual: R$ {desconto_atual:.2f}")

        while True:
            try:
                desconto = float(input("Digite o valor do desconto: R$ "))

                if desconto < 0:
                    print("ERRO: O desconto não pode ser negativo!")

                elif desconto > mensalidade:
                    print("ERRO: O desconto não pode ser maior que a mensalidade!")

                else:
                    self.banco.aplicar_desconto(matricula, desconto)
                    print(f"\nDesconto de R$ {desconto:.2f} aplicado para {nome}.")
                    break

            except ValueError:
                print("ERRO: Digite um valor válido.")



       
    def calcular_valor_final(self, mensalidade, desconto, vencimento):
        valor_original = mensalidade
        valor_com_desconto = valor_original - desconto
        juros = 0.0

        try:
            data_vencimento = datetime.strptime(vencimento, "%d/%m/%Y")

        except ValueError:
            print("ERRO: Data de vencimento inválida no banco.")
            return None

        hoje = datetime.now()

        if hoje > data_vencimento:
            juros = valor_com_desconto * self.taxa_juros

        valor_final = valor_com_desconto + juros

        return valor_original, desconto, juros, valor_final
   
    
    def enviar_boleto_email(self):
        
        print("\nEnvio de boleto por email")

        matricula = self.faculdade.validar_matricula("Digite a matrícula do estudante para enviar o boleto: ")

        dados = self.banco.consultar_financeiro(matricula)
    
        if dados is None:
            estudante = self.banco.buscar_estudante(matricula)

            if estudante is None:
                print("ERRO: Estudante não encontrado!")
            else:
                print("ERRO: Este estudante ainda não possui mensalidade cadastrada.")

            return
        
        nome, email, matricula, mensalidade, desconto, vencimento = dados

        resultado = self.calcular_valor_final(mensalidade, desconto, vencimento)

        if resultado is None:
            return

        valor_original, desconto, juros, valor_final = resultado
        
        print("\n==============================")
        print("BOLETO ENVIADO")
        print("==============================")
        print(f"Para: {email}")
        print(f"Aluno: {nome}")
        print(f"Matrícula: {matricula}")
        print(f"Valor original: R$ {valor_original:.2f}")
        print(f"Desconto: R$ {desconto:.2f}")
        print(f"Juros: R$ {juros:.2f}")
        print(f"Valor final do boleto: R$ {valor_final:.2f}")
        print(f"Vencimento: {vencimento}")
        print("\nMensagem: Boleto enviado automaticamente para o email cadastrado.")
        
           
    def menu_financeiro(self):
        while True:
            print("\nSISTEMA DE CONTROLE FINANCEIRO DOS ESTUDANTES")
            print("1. Definir mensalidade")
            print("2. Consultar mensalidade")
            print("3. Relatório financeiro")
            print("4. Aplicar desconto")
            print("5. Enviar boleto por email")
            print("0. Voltar ao menu principal")

            opcao = input("\nEscolha uma opção: ")

            
            if opcao == "1":
                self.definir_mensalidade()

            elif opcao == "2":
                self.consultar_mensalidade()

            elif opcao == "3":
                self.relatorio_financeiro()

            elif opcao == "4":
                self.aplicar_desconto()

            elif opcao == "5":
                self.enviar_boleto_email()

            elif opcao == "0":
                print("\nVoltando ao menu principal.")
                break

            else:
                print("\nOpção inválida!")
