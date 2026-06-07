import sqlite3
from colaborador import Colaborador
from financas import Financas

# -------------------------
# BENEFÍCIOS DISPONÍVEIS
# -------------------------

BENEFICIOS_DISPONIVEIS = [
    ("Vale Transporte", 200),
    ("Vale Refeição", 400),
    ("Plano de Saúde", 600)
]

# -------------------------
# BANCO DE DADOS
# -------------------------

def criar_tabelas():

    with sqlite3.connect("folha.db") as conn:

        cursor = conn.cursor()

        # -------------------------
        # TABELA DE COLABORADORES
        # -------------------------

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS colaboradores (

                matricula INTEGER
                PRIMARY KEY AUTOINCREMENT,

                nome TEXT NOT NULL,

                cargo TEXT NOT NULL,

                salario REAL NOT NULL,

                dependentes INTEGER NOT NULL
            )
        """)

        # -------------------------
        # TABELA DE BENEFÍCIOS
        # -------------------------

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS beneficios (

                id INTEGER
                PRIMARY KEY AUTOINCREMENT,

                nome TEXT UNIQUE NOT NULL,

                valor REAL NOT NULL
            )
        """)

        # -------------------------
        # RELAÇÃO COLABORADOR X BENEFÍCIOS
        # -------------------------

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS colaborador_beneficios (

                colaborador_id INTEGER,

                beneficio_id INTEGER,

                FOREIGN KEY (colaborador_id)
                    REFERENCES colaboradores(matricula),

                FOREIGN KEY (beneficio_id)
                    REFERENCES beneficios(id)
            )
        """)

        # -------------------------
        # INSERIR BENEFÍCIOS PADRÃO
        # -------------------------

        cursor.executemany("""
            INSERT OR IGNORE INTO beneficios (
                nome,
                valor
            )
            VALUES (?, ?)
        """, BENEFICIOS_DISPONIVEIS)

# -------------------------
# CRUD
# -------------------------

def salvar_colaborador(colaborador):

    with sqlite3.connect("folha.db") as conn:

        cursor = conn.cursor()

        # -------------------------
        # SALVAR COLABORADOR
        # -------------------------

        cursor.execute("""
            INSERT INTO colaboradores (

                nome,
                cargo,
                salario,
                dependentes

            )
            VALUES (?, ?, ?, ?)
        """, (

            colaborador.nome,
            colaborador.cargo,
            colaborador.salario,
            colaborador.dependentes
        ))

        colaborador_id = cursor.lastrowid

        # -------------------------
        # SALVAR BENEFÍCIOS
        # -------------------------

        for beneficio_nome in colaborador.beneficios:

            cursor.execute("""
                SELECT id
                FROM beneficios
                WHERE nome = ?
            """, (beneficio_nome,))

            resultado = cursor.fetchone()

            if resultado:

                beneficio_id = resultado[0]

                cursor.execute("""
                    INSERT INTO colaborador_beneficios (

                        colaborador_id,
                        beneficio_id

                    )
                    VALUES (?, ?)
                """, (

                    colaborador_id,
                    beneficio_id
                ))

def carregar_colaboradores():

    with sqlite3.connect("folha.db") as conn:

        cursor = conn.cursor()

        cursor.execute("""
            SELECT *
            FROM colaboradores
        """)

        rows = cursor.fetchall()

        colaboradores = []

        for r in rows:

            colaborador_id = r[0]

            # -------------------------
            # BUSCAR BENEFÍCIOS
            # -------------------------

            cursor.execute("""
                SELECT b.nome

                FROM beneficios b

                INNER JOIN colaborador_beneficios cb
                    ON b.id = cb.beneficio_id

                WHERE cb.colaborador_id = ?
            """, (colaborador_id,))

            beneficios = [
                b[0]
                for b in cursor.fetchall()
            ]

            colaboradores.append(

                Colaborador(

                    nome=r[1],
                    cargo=r[2],
                    salario=r[3],
                    matricula=r[0],
                    dependentes=r[4],
                    beneficios=beneficios
                )
            )

        return colaboradores

# -------------------------
# INTERFACE
# -------------------------

def escolher_beneficios():

    print("\nEscolha os benefícios:")
    print("(separados por vírgula)")

    for i, beneficio in enumerate(
        BENEFICIOS_DISPONIVEIS,
        start=1
    ):

        print(f"{i} - {beneficio[0]}")

    escolha = input(
        "Digite os números desejados: "
    )

    beneficios_escolhidos = []

    if escolha:

        indices = escolha.split(",")

        for i in indices:

            i = i.strip()

            if (
                i.isdigit()
                and 1 <= int(i) <= len(BENEFICIOS_DISPONIVEIS)
            ):

                beneficios_escolhidos.append(
                    BENEFICIOS_DISPONIVEIS[
                        int(i) - 1
                    ][0]
                )

            else:
                print(f"Índice inválido: {i}")

    return beneficios_escolhidos

def cadastrar():

    print("\n=== CADASTRO DE COLABORADOR ===")

    nome = input("Nome: ").strip()

    cargo = input("Cargo: ").strip()

    if not nome:

        print("Nome inválido.")
        return

    if not cargo:

        print("Cargo inválido.")
        return

    try:

        salario = float(
            input("Salário: R$ ")
        )

        dependentes = int(
            input("Número de dependentes: ")
        )

        if salario < 0:

            print("Salário inválido.")
            return

        if dependentes < 0:

            print("Número de dependentes inválido.")
            return

    except ValueError:

        print("Erro nos valores digitados.")
        return

    beneficios = escolher_beneficios()

    colaborador = Colaborador(

        nome=nome,
        cargo=cargo,
        salario=salario,
        matricula=0,
        dependentes=dependentes,
        beneficios=beneficios
    )

    salvar_colaborador(colaborador)

    print(
        "\nColaborador cadastrado com sucesso!"
    )

def listar():

    print("\n=== LISTA DE COLABORADORES ===")

    colaboradores = carregar_colaboradores()

    if not colaboradores:

        print("Nenhum colaborador cadastrado.")
        return

    for i, colaborador in enumerate(
        colaboradores,
        start=1
    ):

        print(f"{i} - {colaborador}")

def gerar_holerite():

    colaboradores = carregar_colaboradores()

    if not colaboradores:

        print("Nenhum colaborador cadastrado.")
        return

    listar()

    try:

        indice = int(
            input(
                "\nDigite o número do colaborador: "
            )
        ) - 1

        colaborador = colaboradores[indice]

    except (ValueError, IndexError):

        print("Índice inválido.")
        return

    financas = Financas(colaborador)

    print(
        financas.gerar_holerite()
    )

# -------------------------
# MENU
# -------------------------

def menu():

    criar_tabelas()

    while True:

        print("\n===== SISTEMA DE FOLHA DE PAGAMENTO =====")

        print("1 - Cadastrar colaborador")

        print("2 - Listar colaboradores")

        print("3 - Gerar holerite")

        print("0 - Sair")

        opcao = input("\nEscolha: ")

        if opcao == "1":

            cadastrar()

        elif opcao == "2":

            listar()

        elif opcao == "3":

            gerar_holerite()

        elif opcao == "0":

            print("\nEncerrando sistema...")
            break

        else:

            print("Opção inválida.")

# -------------------------
# EXECUÇÃO
# -------------------------

if __name__ == "__main__":
    menu()
