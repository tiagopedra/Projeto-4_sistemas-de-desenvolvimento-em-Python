import sqlite3
from estudantes import Estudante


class BancoDeDados:
    def __init__(self, nome_banco="faculdade.db"):
        self.nome_banco = nome_banco

        self.criar_tabelas()

    def conectar(self):
        return sqlite3.connect(self.nome_banco)

    def criar_tabelas(self):
        conexao = self.conectar()
        cursor = conexao.cursor()

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS estudantes (
                matricula INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                email TEXT NOT NULL,
                nota1 REAL NOT NULL,
                nota2 REAL NOT NULL
            )
        """)

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS financeiro (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                matricula INTEGER NOT NULL UNIQUE,
                mensalidade REAL NOT NULL,
                desconto REAL DEFAULT 0,
                vencimento TEXT NOT NULL,
                FOREIGN KEY (matricula) REFERENCES estudantes(matricula)
            )
        """)

        conexao.commit()
        conexao.close()


    def cadastrar_estudante(self, nome, email, nota1, nota2):
        conexao = self.conectar()
        cursor = conexao.cursor()

        cursor.execute("""
            INSERT INTO estudantes (nome, email, nota1, nota2)
            VALUES (?, ?, ?, ?)
        """, (nome, email, nota1, nota2))

        conexao.commit()

        matricula = cursor.lastrowid

        conexao.close()

        return matricula

    def listar_estudantes(self):
        conexao = self.conectar()
        cursor = conexao.cursor()

        cursor.execute("""
            SELECT matricula, nome, email, nota1, nota2
            FROM estudantes
            ORDER BY matricula
        """)

        dados = cursor.fetchall()
        conexao.close()

        estudantes = []

        for matricula, nome, email, nota1, nota2 in dados:
            estudante = Estudante(matricula, nome, email, nota1, nota2)
            estudantes.append(estudante)

        return estudantes

    def buscar_estudante(self, matricula):
        conexao = self.conectar()
        cursor = conexao.cursor()

        cursor.execute("""
            SELECT matricula, nome, email, nota1, nota2
            FROM estudantes
            WHERE matricula = ?
        """, (matricula,))

        dado = cursor.fetchone()
        conexao.close()

        if dado is None:
            return None

        matricula, nome, email, nota1, nota2 = dado
        return Estudante(matricula, nome, email, nota1, nota2)

    def atualizar_estudante(self, matricula, nome, email, nota1, nota2):
        conexao = self.conectar()
        cursor = conexao.cursor()

        cursor.execute("""
            UPDATE estudantes
            SET nome = ?, email = ?, nota1 = ?, nota2 = ?
            WHERE matricula = ?
        """, (nome, email, nota1, nota2, matricula))

        conexao.commit()
        conexao.close()

    def excluir_estudante(self, matricula):
        conexao = self.conectar()
        cursor = conexao.cursor()

        cursor.execute("""
            DELETE FROM financeiro
            WHERE matricula = ?
        """, (matricula,))

        cursor.execute("""
            DELETE FROM estudantes
            WHERE matricula = ?
        """, (matricula,))

        conexao.commit()
        conexao.close()

    def contar_estudantes(self):
        conexao = self.conectar()
        cursor = conexao.cursor()

        cursor.execute("SELECT COUNT(*) FROM estudantes")
        total = cursor.fetchone()[0]

        conexao.close()

        return total



    def definir_mensalidade(self, matricula, mensalidade, vencimento):
        conexao = self.conectar()
        cursor = conexao.cursor()

        cursor.execute("""
            SELECT id
            FROM financeiro
            WHERE matricula = ?
        """, (matricula,))

        existe = cursor.fetchone()

        if existe:
            cursor.execute("""
                UPDATE financeiro
                SET mensalidade = ?, vencimento = ?
                WHERE matricula = ?
            """, (mensalidade, vencimento, matricula))
        else:
            cursor.execute("""
                INSERT INTO financeiro (matricula, mensalidade, desconto, vencimento)
                VALUES (?, ?, 0, ?)
            """, (matricula, mensalidade, vencimento))

        conexao.commit()
        conexao.close()

    def consultar_financeiro(self, matricula):
        conexao = self.conectar()
        cursor = conexao.cursor()

        cursor.execute("""
            SELECT estudantes.nome,
                   estudantes.email,
                   estudantes.matricula,
                   financeiro.mensalidade,
                   financeiro.desconto,
                   financeiro.vencimento
            FROM estudantes
            INNER JOIN financeiro
            ON estudantes.matricula = financeiro.matricula
            WHERE estudantes.matricula = ?
        """, (matricula,))

        resultado = cursor.fetchone()

        conexao.close()

        return resultado

    def aplicar_desconto(self, matricula, desconto):
        conexao = self.conectar()
        cursor = conexao.cursor()

        cursor.execute("""
            UPDATE financeiro
            SET desconto = ?
            WHERE matricula = ?
        """, (desconto, matricula))

        conexao.commit()
        conexao.close()

    def relatorio_financeiro(self):
        conexao = self.conectar()
        cursor = conexao.cursor()

        cursor.execute("""
            SELECT estudantes.matricula,
                   estudantes.nome,
                   estudantes.email,
                   financeiro.mensalidade,
                   financeiro.desconto,
                   financeiro.vencimento
            FROM estudantes
            INNER JOIN financeiro
            ON estudantes.matricula = financeiro.matricula
            ORDER BY estudantes.matricula
        """)

        dados = cursor.fetchall()

        conexao.close()

        return dados


    def cadastrar_100_estudantes_com_financeiro(self):
    
        if self.contar_estudantes() >= 100:
            print("O banco já possui 100 ou mais estudantes cadastrados.")
            return

        conexao = self.conectar()
        cursor = conexao.cursor()

        for i in range(1, 101):
            nome = f"Estudante {i}"
            email = f"estudante{i}@email.com"

            nota1 = float((i % 10) + 1)
            nota2 = float(((i + 3) % 10) + 1)

            cursor.execute("""
                INSERT INTO estudantes (nome, email, nota1, nota2)
                VALUES (?, ?, ?, ?)
            """, (nome, email, nota1, nota2))

            matricula = cursor.lastrowid

            mensalidade = 700.00 + (i * 5)

            if i % 5 == 0:
                desconto = 50.00
            elif i % 10 == 0:
                desconto = 100.00
            else:
                desconto = 0.00

            vencimento = "10/12/2026"

            cursor.execute("""
                INSERT INTO financeiro (matricula, mensalidade, desconto, vencimento)
                VALUES (?, ?, ?, ?)
            """, (matricula, mensalidade, desconto, vencimento))

        conexao.commit()
        conexao.close()

        print("100 estudantes com dados financeiros foram cadastrados com sucesso.")
