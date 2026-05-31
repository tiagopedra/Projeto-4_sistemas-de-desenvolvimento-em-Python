import sqlite3
from colaborador import Colaborador
from financas import Financas

BENEFICIOS_DISPONIVEIS = [
    "Vale Transporte",
    "Vale Refeição",
    "Plano de Saúde"
]

# -------------------------
# BANCO DE DADOS
# -------------------------

def criar_tabela():
    conn = sqlite3.connect("folha.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS colaboradores (
            matricula INTEGER PRIMARY KEY,
            nome TEXT,
            cargo TEXT,
            salario REAL,
            dependentes INTEGER,
            beneficios TEXT
        )
    """)
    conn.commit()
    conn.close()

def salvar_colaborador(colaborador):
    conn = sqlite3.connect("folha.db")
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO colaboradores (matricula, nome, cargo, salario, dependentes, beneficios)
        VALUES (?, ?, ?, ?, ?, ?)
    """, (
        colaborador.matricula,
        colaborador.nome,
        colaborador.cargo,
        colaborador.salario,
        colaborador.dependentes,
        ",".join(colaborador.beneficios)
    ))
    conn.commit()
    conn.close()

def carregar_colaboradores():
    conn = sqlite3.connect("folha.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM colaboradores")
    rows = cursor.fetchall()
    conn.close()

    lista = []
    for r in rows:
        lista.append(Colaborador(
            nome=r[1],
            cargo=r[2],
            salario=r[3],
            matricula=r[0],
            dependentes=r[4],
            beneficios=r[5].split(",") if r[5] else []
        ))
    return lista

# -------------------------
# FUNÇÕES DE INTERFACE
# -------------------------

def escolher_beneficios():
    print("\nEscolha os benefícios (separados por vírgula):")
    for i, beneficio in enumerate(BENEFICIOS_DISPONIVEIS):
        print(f"{i} - {beneficio}")

    escolha = input("Digite os números desejados: ")
    beneficios_escolhidos = []

    if escolha:
        indices = escolha.split(",")
        for i in indices:
            i = i.strip()
            if i.isdigit() and int(i) < len(BENEFICIOS_DISPONIVEIS):
                beneficios_escolhidos.append(BENEFICIOS_DISPONIVEIS[int(i)])
            else:
                print(f"Índice inválido: {i}")

    return beneficios_escolhidos

def cadastrar():
    colaboradores = carregar_colaboradores()
    contador_matricula = len(colaboradores) + 1

    print("\n=== CADASTRO DE COLABORADOR ===")
    nome = input("Nome: ")
    cargo = input("Cargo: ")

    try:
        salario = float(input("Salário: R$ "))
        dependentes = int(input("Dependentes: "))
    except ValueError:
        print("Erro nos valores.")
        return

    beneficios = escolher_beneficios()

    colaborador = Colaborador(
        nome=nome,
        cargo=cargo,
        salario=salario,
        matricula=contador_matricula,
        dependentes=dependentes,
        beneficios=beneficios
    )

    salvar_colaborador(colaborador)
    print(f"Colaborador cadastrado! Matrícula: {contador_matricula}")

def listar():
    print("\n=== LISTA DE COLABORADORES ===")
    colaboradores = carregar_colaboradores()
    if not colaboradores:
        print("Nenhum cadastrado.")
        return

    for i, c in enumerate(colaboradores):
        print(f"{i} - {c}")

def gerar_holerite():
    colaboradores = carregar_colaboradores()
    listar()
    if not colaboradores:
        return

    try:
        indice = int(input("Digite o número do colaborador: "))
        colaborador = colaboradores[indice]
    except (ValueError, IndexError):
        print("Índice inválido.")
        return

    financas = Financas(colaborador)
    print(financas.gerar_holerite())

def menu():
    criar_tabela()  # garante que a tabela existe
    while True:
        print("\n===== SISTEMA DE FOLHA DE PAGAMENTO =====")
        print("1 - Cadastrar colaborador")
        print("2 - Listar colaboradores")
        print("3 - Gerar holerite")
        print("0 - Sair")

        opcao = input("Escolha: ")

        if opcao == "1":
            cadastrar()
        elif opcao == "2":
            listar()
        elif opcao == "3":
            gerar_holerite()
        elif opcao == "0":
            print("Encerrando...")
            break
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    menu()
