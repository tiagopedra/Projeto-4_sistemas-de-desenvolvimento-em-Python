# importa a classe Conta que representa cada entidade de conta do sistema
from conta import Conta

# importa a classe datetime para trabalhar com datas
from datetime import datetime

# importa Decimal para cálculos financeiros mais precisos
from decimal import Decimal

# importa sqlite3 para persistência de dados no banco
import sqlite3

# importa random para geração de dados aleatórios
import random

# define a data atual do sistema para comparações
dia_atual = datetime.now().day
mes_atual = datetime.now().month
ano_atual = datetime.now().year

# lista de feriados utilizada para validação de datas
feriados = [
    ["01-01", "Confraternização Universal"],
    ["04-21", "Tiradentes"],
    ["05-01", "Dia do trabalhador"],
    ["09-07", "Independência"],
    ["10-12", "Padroeira do Brasil"],
    ["11-02", "Finados"],
    ["11-15", "Proclamação da República"],
    ["12-25", "Natal"]
]

# Classe responsável pelo gerenciamento das contas e do orçamento
class Cadastro:

    # método construtor que inicializa o sistema
    def __init__(self):

        # cria conexão com banco de dados SQLite
        self.conn = sqlite3.connect("contas.db")
        self.cursor = self.conn.cursor()

        # cria tabela de contas caso não exista
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS contas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT,
            dia INTEGER,
            mes INTEGER,
            ano INTEGER,
            valor REAL,
            status TEXT
        )
        """)

        # cria tabela de orçamento (um único registro)
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS orcamento (
            id INTEGER PRIMARY KEY,
            valor REAL
        )
        """)

        # salva alterações no banco
        self.conn.commit()

        # lista que armazenará objetos Conta carregados do banco
        self.contas = []

        # carrega o orçamento já salvo (se existir)
        self.carregar_orcamento()

        # conjunto usado para controlar alertas já exibidos
        self.alertas_disparados = set()

        # gera contas iniciais (somente na primeira execução)
        self.gerar_contas_iniciais()

        # carrega as contas do banco para a lista em memória
        self.carregar_contas()

    # gera 100 contas automaticamente com dados aleatórios
    def gerar_contas_iniciais(self):

        # verifica quantas contas já existem no banco
        self.cursor.execute("SELECT COUNT(*) FROM contas")
        total = self.cursor.fetchone()[0]

        # se já houver contas, não gera novamente
        if total > 0:
            return

        # cria 100 contas no banco de dados
        for i in range(1, 101):
            nome = f"Conta {i}"

            # gera dia, mês e ano aleatórios
            dia = random.randint(1, 28)
            mes = random.randint(1, 12)
            ano = random.randint(2026, 2030)

            # gera valor aleatório com duas casas decimais
            valor = float(Decimal(random.uniform(10, 1000)).quantize(Decimal("0.01")))
            
            # define data atual e data de vencimento
            data_hoje = datetime.now()
            data_vencimento = datetime(ano, mes, dia)

            # define status com base na data
            if data_vencimento < data_hoje:
                status = "Atrasada"
            else:
                status = "Pendente"

            # insere no banco
            self.cursor.execute("""
            INSERT INTO contas (nome, dia, mes, ano, valor, status)
            VALUES (?, ?, ?, ?, ?, ?)
            """, (nome, dia, mes, ano, valor, status))

        self.conn.commit()

        print("Base inicial com 100 contas criada.")

    # carrega as contas do banco para a lista
    def carregar_contas(self):
       
        self.contas = []

        # busca todas as contas no banco
        self.cursor.execute("""
        SELECT id, nome, dia, mes, ano, valor, status FROM contas
        """)

        dados = self.cursor.fetchall()

        # cria objetos Conta e adiciona na lista
        for linha in dados:
            conta = Conta(
                linha[0],  # id
                linha[1],  # nome
                linha[2],  # dia
                linha[3],  # mes
                linha[4],  # ano
                linha[5],  # valor
                linha[6]   # status
            )
            self.contas.append(conta)

    # carrega o orçamento do banco
    def carregar_orcamento(self):

        # busca o valor do orçamento
        self.cursor.execute("SELECT valor FROM orcamento LIMIT 1")
        resultado = self.cursor.fetchone()

        # se existir, converte para Decimal
        if resultado:
            from decimal import Decimal
            self.orcamento_total = Decimal(resultado[0])
        else:
            self.orcamento_total = 0

    # retorna a lista de contas
    def listar_contas(self):
        return self.contas

    # verifica se uma data é feriado
    def _is_feriado(self, dia, mes, ano):

        data_str = f"{mes:02d}-{dia:02d}"

        # percorre a lista de feriados
        for feriado in feriados:
            if feriado[0] == data_str:
                return feriado[1]

        return None


    # calcula o próximo dia útil
    def _proximo_dia_util(self, dia, mes, ano):
        from datetime import timedelta

        data = datetime(ano, mes, dia)

        while True:
            data += timedelta(days=1)

            nome_feriado = self._is_feriado(data.day, data.month, data.year)

            # verifica se não é fim de semana nem feriado
            if data.weekday() < 5 and not nome_feriado:
                return data.day, data.month, data.year

    # método auxiliar para validar entrada numérica
    def _input_int(self, mensagem, min_val, max_val):
        while True:
            try:
                valor = int(input(mensagem))
                if min_val <= valor <= max_val:
                    return valor
                print(f"Valor inválido. Digite entre {min_val} e {max_val}.")
            except ValueError:
                print("Digite um número válido.")

    # valida se a data é válida
    def _validar_data(self, ano, mes, dia):
        try:
            datetime(ano, mes, dia)
            return True
        except ValueError:
            return False

    # cadastra uma nova conta
    def cadastrar_conta(self):

        # exige orçamento antes do cadastro
        if self.orcamento_total == 0:
            print("\nDefina o orçamento antes de cadastrar contas.")
            return

        # recebe nome da conta
        nome_conta = input("Digite o nome da conta: ").strip().title()

        # coleta data
        ano_vencimento = self._input_int("Digite o ano de vencimento: ", ano_atual, ano_atual + 20)
        mes_vencimento = self._input_int("Digite o mês de vencimento: ", 1, 12)

        # valida o dia
        while True:
            dia_vencimento = self._input_int("Digite o dia do vencimento: ", 1, 31)

            if self._validar_data(ano_vencimento, mes_vencimento, dia_vencimento):

                nome_feriado = self._is_feriado(dia_vencimento, mes_vencimento, ano_vencimento)
                data_temp = datetime(ano_vencimento, mes_vencimento, dia_vencimento)

                # ajusta se for feriado ou fim de semana
                if nome_feriado or data_temp.weekday() >= 5:

                    novo_dia, novo_mes, novo_ano = self._proximo_dia_util(
                        dia_vencimento, mes_vencimento, ano_vencimento
                    )

                    print("\nA data informada é um feriado ou fim de semana.")
                    if nome_feriado:
                        print(f"Feriado: {nome_feriado}")

                    print(f"Novo vencimento será: {novo_dia:02d}/{novo_mes:02d}/{novo_ano}")

                    dia_vencimento = novo_dia
                    mes_vencimento = novo_mes
                    ano_vencimento = novo_ano

                break
            else:
                print("Data inválida. Verifique dia/mês/ano.")

        # coleta valor
        while True:
            try:
                valor = Decimal(input("Digite o valor da conta: "))
                if valor > 0:
                    break
                print("Digite um valor maior que zero.")
            except ValueError:
                print("Digite um valor válido.")

        status = "Pendente"

        # insere no banco
        self.cursor.execute("""
        INSERT INTO contas (nome, dia, mes, ano, valor, status)
        VALUES (?, ?, ?, ?, ?, ?)
        """, (nome_conta, dia_vencimento, mes_vencimento, ano_vencimento, float(valor), status))

        self.conn.commit()

        # recupera o ID gerado
        id_gerado = self.cursor.lastrowid

        # cria objeto em memória
        conta = Conta(
            id_gerado,
            nome_conta,
            dia_vencimento,
            mes_vencimento,
            ano_vencimento,
            valor,
            status
        )

        # adiciona na lista
        self.contas.append(conta)

        # verifica orçamento e dispara alertas
        self.verificar_orcamento()

        print("\nConta cadastrada com sucesso.")

    # define ou atualiza orçamento
    def definir_orcamento(self):
        while True:
            try:
                valor = Decimal(input("Digite o valor do orçamento: "))

                if valor <= 0:
                    print("Digite um valor maior que zero.")
                    continue

                # confirma atualização
                if self.orcamento_total > 0:
                    print(f"\nOrçamento atual: R$ {self.orcamento_total:.2f}")
                    confirmacao = input("Deseja atualizar o orçamento? (s/n): ").lower()

                    if confirmacao != "s":
                        print("Operação cancelada.")
                        return

                # define orçamento
                self.orcamento_total = valor

                # verifica se já existe
                self.cursor.execute("SELECT COUNT(*) FROM orcamento")
                existe = self.cursor.fetchone()[0]

                if existe == 0:
                    self.cursor.execute(
                        "INSERT INTO orcamento (id, valor) VALUES (1, ?)",
                        (float(valor),)
                    )
                else:
                    self.cursor.execute(
                        "UPDATE orcamento SET valor=? WHERE id=1",
                        (float(valor),)
                    )
                    
                self.conn.commit()

                # reseta alertas
                self.alertas_disparados = set()

                print("\nOrçamento definido/atualizado com sucesso.")
                return

            except:
                print("Valor inválido.")

    # soma total de gastos
    def total_gasto(self):
        return sum(Decimal(conta.valor) for conta in self.contas)
    
    # calcula situação do orçamento e exibe alertas
    def verificar_orcamento(self):
        if self.orcamento_total == 0:
            return

        from decimal import Decimal

        total = self.total_gasto()
        percentual = (total / Decimal(self.orcamento_total)) * 100

        restante = Decimal(self.orcamento_total) - total

        print(f"\nAtenção: Total do orçamento já utilizado: R$ {total:.2f}")
        print(f"Atenção: Percentual do orçamento já utilizado: {percentual:.2f}%")
        print(f"Atenção: Saldo restante do orçamento: R$ {restante:.2f}")

        # verifica estouro do orçamento
        if total > self.orcamento_total:
            excedente = total - Decimal(self.orcamento_total)
            print(f"\nOrçamento ultrapassado em R$ {excedente:.2f}")
            return

        # alerta se atingir 100 por cento
        if percentual >= 100 and 100 not in self.alertas_disparados:
            print("\nOrçamento atingido.")
            self.alertas_disparados.add(100)
            return
