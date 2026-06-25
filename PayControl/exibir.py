# importa Decimal para cálculos financeiros precisos
from decimal import Decimal

# importa datetime para manipulação de datas
from datetime import datetime

# classe responsável por exibir informações do sistema para o usuário
class Exibir:

    # método construtor recebe o objeto cadastro
    def __init__(self, cadastro):
        self.cadastro = cadastro

    # método auxiliar para validar entrada numérica inteira dentro de um intervalo
    def _input_int(self, msg, min_val, max_val):
        while True:
            try:
                valor = int(input(msg))
                # verifica se está dentro do intervalo permitido
                if min_val <= valor <= max_val:
                    return valor
                print(f"Digite um valor entre {min_val} e {max_val}")
            except ValueError:
                print("Digite um número válido.")

    # método responsável por listar contas de diversas formas
    def listar_contas(self):

        # recupera lista de contas do cadastro
        contas = self.cadastro.listar_contas()

        # verifica se existem contas
        if not contas:
            print("\nNenhuma conta cadastrada.")
            return

        # menu de opções de listagem
        print("\n### FILTRO DE LISTAGEM ###")
        print("[1] Todas as contas")
        print("[2] Contas por status")
        print("[3] Contas por valor")
        print("[4] Contas por período e status")
        print("[5] Ordenar por impacto no orçamento")

        # captura opção do usuário
        try:
            opcao = int(input("Escolha uma opção: "))
        except ValueError:
            print("Opção inválida.")
            return

        # lista todas as contas
        if opcao == 1:
            print("\n### LISTA DE CONTAS ###")
            for conta in contas:
                conta.exibir_dados()

        # lista contas filtradas por status
        elif opcao == 2:
            print("\nEscolha o status:")
            print("[1] Pendente")
            print("[2] Atrasada")
            print("[3] Paga")

            try:
                opcao_status = int(input("Digite a opção: "))
            except ValueError:
                print("Opção inválida.")
                return

            # define filtro
            if opcao_status == 1:
                status_filtro = "Pendente"
            elif opcao_status == 2:
                status_filtro = "Atrasada"
            elif opcao_status == 3:
                status_filtro = "Paga"
            else:
                print("Opção inválida.")
                return

            # aplica filtro usando list comprehension
            filtradas = [conta for conta in contas if conta.status == status_filtro]

            if not filtradas:
                print("\nNenhuma conta encontrada.")
            else:
                for conta in filtradas:
                    conta.exibir_dados()

        # lista contas filtradas por valor
        elif opcao == 3:
            try:
                valor = float(input("Digite o valor: "))
            except ValueError:
                print("Valor inválido.")
                return

            # compara valor das contas
            filtradas = [conta for conta in contas if Decimal(conta.valor) == valor]

            if not filtradas:
                print("\nNenhuma conta encontrada.")
            else:
                for conta in filtradas:
                    conta.exibir_dados()

        # lista contas por período (mês e ano) e status
        elif opcao == 4:
            try:
                mes = self._input_int("Digite o mês: ", 1, 12)
                ano = self._input_int("Digite o ano: ", 2026, 2040)
            except:
                print("Entrada inválida.")
                return

            print("\nEscolha o status:")
            print("[1] Pendente")
            print("[2] Atrasada")
            print("[3] Paga")

            try:
                opcao_status = int(input("Digite a opção: "))
            except ValueError:
                print("Opção inválida.")
                return

            # define status de filtro
            if opcao_status == 1:
                status_filtro = "Pendente"
            elif opcao_status == 2:
                status_filtro = "Atrasada"
            elif opcao_status == 3:
                status_filtro = "Paga"
            else:
                print("Opção inválida.")
                return

            # filtra contas com base em mês, ano e status
            filtradas = [
                conta for conta in contas
                if conta.mes_vencimento == mes
                and conta.ano_vencimento == ano
                and conta.status == status_filtro
            ]

            if not filtradas:
                print("\nNenhuma conta encontrada.")
            else:
                for conta in filtradas:
                    conta.exibir_dados()

        # ordena contas por impacto (valor mais alto primeiro)
        elif opcao == 5:

            # usa sorted com função lambda para ordenar
            ordenadas = sorted(contas, key=lambda conta: float(conta.valor), reverse=True)

            print("\n### CONTAS ORDENADAS POR IMPACTO ###")

            for conta in ordenadas:
                conta.exibir_dados()

        else:
            print("Opção inválida.")
        
        # após qualquer listagem, verifica e mostra situação do orçamento
        self.cadastro.verificar_orcamento()

    # método de pesquisa de contas com múltiplos critérios
    def pesquisar_contas(self):

        print("\nEscolha a forma de consulta:\n")
        print("[1] Id da Conta")
        print("[2] Nome da Conta")
        print("[3] Valor da Conta")
        print("[4] Mês de vencimento")
        print("[5] Dia de vencimento")
        print("[6] Ano de vencimento")

        try:
            opcao = int(input("\nEscolha uma opção: "))
        except ValueError:
            print("Digite um número válido.")
            return

        contas = self.cadastro.listar_contas()

        if not contas:
            print("\nNenhuma conta cadastrada.")
            return

        resultados = []

        # busca por ID (precisa e única)
        if opcao == 1:
            try:
                id_busca = int(input("Digite o ID da conta: "))
            except ValueError:
                print("ID inválido.")
                return

            resultados = [conta for conta in contas if conta.id == id_busca]
        
        # busca por nome parcial
        elif opcao == 2:
            nome = input("Digite o nome da conta: ").strip().lower()
            resultados = [conta for conta in contas if nome in conta.nome_conta.lower()]

        # busca por valor
        elif opcao == 3:
            while True:
                try:
                    valor = Decimal(input("Digite o valor da conta: "))
                    break
                except:
                    print("Valor inválido.")

            resultados = [conta for conta in contas if conta.valor == valor]

        # busca por mês
        elif opcao == 4:
            mes = self._input_int("Digite o mês: ", 1, 12)
            resultados = [conta for conta in contas if conta.mes_vencimento == mes]

        # busca por dia
        elif opcao == 5:
            dia = self._input_int("Digite o dia: ", 1, 31)
            resultados = [conta for conta in contas if conta.dia_vencimento == dia]

        # busca por ano
        elif opcao == 6:
            ano_atual = datetime.now().year
            ano = self._input_int("Digite o ano: ", ano_atual, ano_atual + 20)
            resultados = [conta for conta in contas if conta.ano_vencimento == ano]

        else:
            print("Opção inválida.")
            return

        # exibe resultados
        if not resultados:
            print("\nNenhuma conta encontrada.")
        else:
            print("\n### RESULTADOS ###")
            for conta in resultados:
                conta.exibir_dados()
    
    # método para exibir relatório detalhado do orçamento
    def relatorio_orcamento_detalhado(self):

        from decimal import Decimal

        # verifica se orçamento foi definido
        if self.cadastro.orcamento_total == 0:
            print("\nNenhum orçamento definido.")
            return

        contas = self.cadastro.listar_contas()

        if not contas:
            print("\nNenhuma conta cadastrada.")
            return

        # converte orçamento para Decimal para precisão
        orcamento = Decimal(str(self.cadastro.orcamento_total))

        # calcula total gasto
        total_gasto = sum(Decimal(str(conta.valor)) for conta in contas)

        percentual = (total_gasto / orcamento) * Decimal("100")
        saldo = orcamento - total_gasto

        print("\n######## RELATÓRIO DE ORÇAMENTO ########")

        print(f"\nOrçamento total: R$ {orcamento:.2f}")
        print(f"Total utilizado: R$ {total_gasto:.2f}")
        print(f"Percentual utilizado: {percentual:.2f}%")
        print(f"Saldo restante: R$ {saldo:.2f}")

        # caso exceda orçamento
        if total_gasto > orcamento:
            excedente = total_gasto - orcamento
            print(f"Excedente: R$ {excedente:.2f}")

        # cálculo de gastos por mês e ano
        print("\n--- Gastos por mês/ano ---")

        resumo = {}

        # agrupa valores por mês e ano
        for conta in contas:
            chave = (conta.mes_vencimento, conta.ano_vencimento)

            if chave not in resumo:
                resumo[chave] = Decimal("0")

            resumo[chave] += Decimal(str(conta.valor))

        # ordena cronologicamente e imprime
        for (mes, ano) in sorted(resumo.keys(), key=lambda x: (x[1], x[0])):
            valor = resumo[(mes, ano)]
            print(f"{mes:02d}/{ano} -> R$ {valor:.2f}")

        print("\n######## FIM DO RELATÓRIO ########\n")