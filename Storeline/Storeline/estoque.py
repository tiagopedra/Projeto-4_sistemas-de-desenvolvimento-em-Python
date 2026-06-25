#IMPORTA A ROUPA
import sqlite3

#CRIA CLASSE ESTOQUE
class Estoque:

    #MÉTODO CONSTRUTOR DO ESTOQUE E CONFIGURAÇÃO DO BANCO DE DADOS
    def __init__(self):
        self.total_vendido = 0
        self.total_pecas_vendidas = 0

        self.conexao = sqlite3.connect("loja.db")
        self.cursor = self.conexao.cursor()

        #CRIA A TABELA ROUPAS
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS roupas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT,
            codigo INTEGER UNIQUE,
            quantidade INTEGER,
            valor REAL
        )
        """)

        #CRIA A TABELA VENDAS
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS vendas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            cliente_id INTEGER,
            roupa_nome TEXT,
            quantidade INTEGER,
            valor_total REAL,
            FOREIGN KEY (cliente_id) REFERENCES clientes(id)
        )
        """)
        self.conexao.commit()


    #EXIBE TODAS AS ROUPAS CADASTRADAS NO ESTOQUE
    def sistema_estoque(self):
        print("\nESTOQUE DE ROUPAS:")
        print("-=" * 15)

        self.cursor.execute("SELECT * FROM roupas")
        roupas = self.cursor.fetchall()

        if len(roupas) == 0:
            print("Ainda não temos roupas cadastradas.")
        else:
            for roupa in roupas:
                print(f"Peça de roupa: {roupa[1]}")
                print(f"ID: {roupa[2]}")
                print(f"Quantidade: {roupa[3]}")
                print(f"Valor: R${roupa[4]:.2f}")
                print("-=" * 15)

    #CRIA O MÉTODO PARA CADASTRAR ROUPA
    def cadastrar_roupa(self):
        while True:
            nome = input("Digite a peça de roupa: ").strip()
            if len(nome) < 3:
                print("Erro! O nome deve ter pelo menos 3 caracteres.")
                continue
            if nome.isdigit():
                print("Erro! O nome não pode conter apenas números.")
                continue
            break

        while True:
            while True:
                try:
                    codigo = int(input("Código [ID]: "))
                    if codigo <= 0:
                        print("Erro! O ID deve ser maior que zero.")
                        continue
                    self.cursor.execute(
                        "SELECT * FROM roupas WHERE codigo = ?",
                        (codigo,)
                    )
                    idigual = self.cursor.fetchone()
                    if idigual:
                        print("Já existe roupa cadastrada com esse ID.")
                        continue
                    break
                except ValueError:
                    print("Erro! Digite apenas números inteiros.")

            while True:
                try:
                    quantidade = int(input("Quantidade da roupa: "))
                    if quantidade <= 0:
                        print('Cadastre uma quantidade maior que zero.')
                        continue
                    break
                    
                except ValueError:
                    print("Erro! Digite apenas números inteiros.")
            while True:
                try:
                    valor = float(input("Valor da roupa R$: "))
                    if valor <= 0:
                        print('Cadastre um valor maior que zero.')
                        continue
                    break

                except ValueError:
                    print("Erro! Digite apenas valores numéricos.")

            self.cursor.execute("""
            INSERT INTO roupas (nome, codigo, quantidade, valor)
            VALUES (?, ?, ?, ?)
            """, (nome, codigo, quantidade, valor))

            self.conexao.commit()

            print("\nRoupa cadastrada com sucesso!")
            break


    #MÉTODO QUE REMOVE A ROUPA
    def remover_roupa(self):
        while True:
            try:
                codigo = int(input("Digite o ID da roupa que deseja remover: "))
                if codigo <= 0:
                    print("Erro! O ID deve ser maior que zero.")
                    continue
                break
            except ValueError:
                print("Erro! Digite apenas números inteiros.")
        self.cursor.execute(
            "SELECT * FROM roupas WHERE codigo = ?",
            (codigo,)
        )
        resultado = self.cursor.fetchone()
        if resultado:
            self.cursor.execute(
                "DELETE FROM roupas WHERE codigo = ?",
                (codigo,)
            )
            self.conexao.commit()
            print("Roupa removida com sucesso!")
        else:
            print("Roupa não encontrada.")

    #GERA O RELATÓRIO GERAL DE ESTOQUE E VENDAS
    def relatorio(self):

        self.cursor.execute(
            "SELECT SUM(quantidade) FROM roupas"
        )
        total_estoque = self.cursor.fetchone()[0]

        if total_estoque is None:
            total_estoque = 0

        self.cursor.execute(
            "SELECT SUM(quantidade) FROM vendas"
        )
        total_vendido_pecas = self.cursor.fetchone()[0]

        if total_vendido_pecas is None:
            total_vendido_pecas = 0

        self.cursor.execute(
            "SELECT SUM(valor_total) FROM vendas"
        )
        total_vendas = self.cursor.fetchone()[0]

        if total_vendas is None:
            total_vendas = 0

        print("\nRELATÓRIO GERAL")
        print("-=" * 15)
        print(f"Peças em estoque: {total_estoque}")
        print(f"Peças vendidas: {total_vendido_pecas}")
        print(f"Total vendido: R${total_vendas:.2f}")

