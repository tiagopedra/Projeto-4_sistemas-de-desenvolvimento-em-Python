# importa Decimal para cálculos financeiros com precisão
from decimal import Decimal

# importa datetime para validações de data
from datetime import datetime

# obtém o ano atual para ser usado como base de validação
ano_atual = datetime.now().year

# classe responsável por realizar cálculos relacionados às contas
class Calculo:

    # método construtor que recebe o objeto cadastro
    # cadastro contém a lista de contas e os dados do sistema
    def __init__(self, cadastro):
        self.cadastro = cadastro

    # método auxiliar para validar entrada numérica dentro de um intervalo
    def _input_int(self, mensagem, min_val, max_val):
        while True:
            try:
                valor = int(input(mensagem))

                # verifica se o valor está dentro do intervalo permitido
                if min_val <= valor <= max_val:
                    return valor

                print(f"Valor inválido. Digite entre {min_val} e {max_val}.")

            except ValueError:
                print("Entrada inválida. Digite um número.")

    # método que valida se uma data é válida (ex: evita 30 de fevereiro)
    def _validar_data(self, ano, mes, dia):
        try:
            datetime(ano, mes, dia)
            return True
        except ValueError:
            return False

    # método principal para cálculo de valores das contas
    def total(self):

        # verifica se existem contas cadastradas
        if not self.cadastro.contas:
            print("\nNenhuma conta cadastrada.")
            return

        # mantém o menu ativo até o usuário fazer uma escolha válida
        while True:
            try:
                print("\n## Escolha a Forma de Cálculo ##")
                print("[1] Calcular valor de todas as contas")
                print("[2] Calcular Valor pelo dia do vencimento")
                print("[3] Calcular Valor pelo mês do Vencimento")
                print("[4] Calcular Valor pelo ano do Vencimento")

                # recebe a opção escolhida pelo usuário
                opcao = int(input("Digite sua opção: "))

                # cálculo do valor total de todas as contas
                if opcao == 1:

                    # soma todos os valores das contas
                    total = sum(
                        Decimal(conta.valor)
                        for conta in self.cadastro.contas
                    )

                    # exibe o resultado formatado
                    print(f"\nTotal geral de todas as contas: R$ {total:.2f}\n")
                    break

                # cálculo pelo dia de vencimento (data completa)
                elif opcao == 2:

                    # entrada e validação da data
                    while True:
                        dia = self._input_int("Dia: ", 1, 31)
                        mes = self._input_int("Mês: ", 1, 12)
                        ano = self._input_int("Ano: ", ano_atual, ano_atual + 20)

                        # valida se a data é válida
                        if self._validar_data(ano, mes, dia):
                            break
                        print("Data inválida.")

                    # soma apenas contas que correspondem à data informada
                    total = sum(
                        Decimal(conta.valor)
                        for conta in self.cadastro.contas
                        if (
                            conta.dia_vencimento == dia and
                            conta.mes_vencimento == mes and
                            conta.ano_vencimento == ano
                        )
                    )

                    # exibe o total encontrado
                    print(f"\nTotal em {dia:02d}/{mes:02d}/{ano}: R$ {total:.2f}\n")
                    break

                # cálculo por mês e ano
                elif opcao == 3:

                    # entrada de dados
                    mes = self._input_int("Mês: ", 1, 12)
                    ano = self._input_int("Ano: ", ano_atual, ano_atual + 20)

                    # soma valores das contas que correspondem ao mês/ano
                    total = sum(
                        Decimal(conta.valor)
                        for conta in self.cadastro.contas
                        if (
                            conta.mes_vencimento == mes and
                            conta.ano_vencimento == ano
                        )
                    )

                    # exibe resultado
                    print(f"\nTotal em {mes:02d}/{ano}: R$ {total:.2f}\n")
                    break

                # cálculo por ano
                elif opcao == 4:

                    # entrada do ano
                    ano = self._input_int("Ano: ", ano_atual, ano_atual + 20)

                    # soma valores das contas daquele ano
                    total = sum(
                        Decimal(conta.valor)
                        for conta in self.cadastro.contas
                        if conta.ano_vencimento == ano
                    )

                    # exibe resultado
                    print(f"\nTotal no ano {ano}: R$ {total:.2f}\n")
                    break

                # caso escolha inválida
                else:
                    print("Escolha uma opção válida.")

            # tratamento de erro caso a entrada não seja número
            except ValueError:
                print("Digite uma opção válida.")