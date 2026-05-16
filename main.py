from colaborador import Colaborador
from financas import Financas

colaboradores = []
contador_matricula = 1

BENEFICIOS_DISPONIVEIS = [
    "Vale Transporte",
    "Vale Refeição",
    "Plano de Saúde"
]


def escolher_beneficios():
    print("\nEscolha os benefícios (separados por vírgula):")
    for i, beneficio in enumerate(BENEFICIOS_DISPONIVEIS):
        print(f"{i} - {beneficio}")

    escolha = input("Digite os números desejados: ")
    beneficios_escolhidos = []

    if escolha:
        try:
            indices = escolha.split(",")
            for i in indices:
                beneficio = BENEFICIOS_DISPONIVEIS[int(i.strip())]
                beneficios_escolhidos.append(beneficio)
        except:
            print("Entrada inválida.")

    return beneficios_escolhidos


def cadastrar():
    global contador_matricula

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

    colaboradores.append(colaborador)
    print(f"Colaborador cadastrado! Matrícula: {contador_matricula}")

    contador_matricula += 1


def listar():
    print("\n=== LISTA DE COLABORADORES ===")
    if not colaboradores:
        print("Nenhum cadastrado.")
        return

    for i, c in enumerate(colaboradores):
        print(f"{i} - {c}")


def gerar_holerite():
    listar()
    if not colaboradores:
        return

    try:
        indice = int(input("Digite o número do colaborador: "))
        colaborador = colaboradores[indice]
    except:
        print("Índice inválido.")
        return

    financas = Financas(colaborador)
    print(financas.gerar_holerite())


def menu():
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