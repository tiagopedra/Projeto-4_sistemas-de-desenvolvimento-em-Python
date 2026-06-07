class Cliente:

    def __init__(self, estoque):
        self.estoque = estoque
        self.cursor = estoque.cursor
        self.conexao = estoque.conexao

        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS clientes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT,
            cpf TEXT UNIQUE,
            cashback REAL DEFAULT 0
        ) 
        """)

        self.conexao.commit()

    #MOSTRAR CLIENTES CADASTRADOS
    def listar_clientes(self):

        self.cursor.execute(
            "SELECT * FROM clientes"
        )

        clientes = self.cursor.fetchall()

        print("\nCLIENTES CADASTRADOS")
        print("-=" * 15)

        if len(clientes) == 0:
            print("Nenhum cliente cadastrado.")
            return

        for cliente in clientes:
            print(f"Nome: {cliente[1]}")
            print(f"CPF: {cliente[2]}")
            print(f"Cashback: R${cliente[3]:.2f}")
            print("-=" * 15)

