import sqlite3
from catalogo import gerar_produtos_iniciais

def criar_banco():

    conexao=sqlite3.connect("loja_vendas.db")
    cursor=conexao.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS produtos(
        prod INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        categoria TEXT NOT NULL,
        preco REAL NOT NULL
    )
    """)

    cursor.execute("SELECT COUNT(*) FROM produtos")
    quantidade=cursor.fetchone()[0]

    if quantidade==0:
        produtos=gerar_produtos_iniciais()

        for produto in produtos:
            cursor.execute("""
            INSERT INTO produtos(nome,categoria,preco)
            VALUES(?,?,?)
            """,produto)

    conexao.commit()
    conexao.close()