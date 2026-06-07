from utils import obter_data_atual, carregar_dados, salvar_dados, gerar_senha_padrao

ARQUIVO_FUNCIONARIOS = "funcionarios.json"

CARGOS = (
    ("1", "Estagiário"),
    ("2", "Júnior"),
    ("3", "Pleno"),
    ("4", "Sênior"),
    ("5", "Gerente"),
)

MAPEAMENTO_CARGA_HORARIA = {
    "12x36": 180,
    "44h semanais": 220,
    "40h semanais": 200,
    "30h semanais": 150,
    "20h semanais": 100,
}


# ============================================================
# PERSISTÊNCIA E BUSCA
# ============================================================

def carregar_funcionarios():
    """Carrega todos os funcionários do JSON."""
    return carregar_dados(ARQUIVO_FUNCIONARIOS)


def salvar_funcionarios(lista_funcionarios):
    """Salva todos os funcionários no JSON."""
    return salvar_dados(lista_funcionarios, ARQUIVO_FUNCIONARIOS)


def gerar_novo_id_funcionario(lista_funcionarios):
    """Gera o próximo ID disponível para funcionário."""
    if not lista_funcionarios:
        return 1

    ids_existentes = []
    for funcionario in lista_funcionarios:
        ids_existentes.append(funcionario.get("id_funcionario", 0))

    return max(ids_existentes) + 1


def buscar_funcionario_id(lista_funcionarios, id_funcionario):
    """Busca um funcionário pelo ID."""
    for funcionario in lista_funcionarios:
        if funcionario.get("id_funcionario") == id_funcionario:
            return funcionario

    return None


# ============================================================
# REGRAS DE NEGÓCIO
# ============================================================

def existe_gerente(lista_funcionarios):
    """Verifica se já existe um gerente cadastrado."""
    for funcionario in lista_funcionarios:
        if funcionario.get("cargo") == "Gerente":
            return True

    return False


def obter_cargo_por_opcao(opcao):
    """Retorna o cargo correspondente à opção digitada."""
    for codigo, cargo in CARGOS:
        if codigo == opcao:
            return cargo

    return None


def obter_horas_mensais_por_carga(carga_horaria):
    """Retorna as horas mensais de acordo com o modelo de carga horária."""
    return MAPEAMENTO_CARGA_HORARIA.get(carga_horaria, 220)


def autenticar_gerente():
    """Valida acesso de gerente usando ID, senha e cargo."""
    lista_funcionarios = carregar_funcionarios()

    print("\n" + "=" * 50)
    print("AUTENTICAÇÃO DE GERENTE")
    print("=" * 50)

    id_digitado = input("Digite o ID do gerente: ").strip()
    senha_digitada = input("Digite a senha: ").strip()

    for funcionario in lista_funcionarios:
        id_funcionario = str(funcionario.get("id_funcionario"))
        senha_funcionario = funcionario.get("senha")
        cargo_funcionario = funcionario.get("cargo")

        if (
            id_funcionario == id_digitado
            and senha_funcionario == senha_digitada
            and cargo_funcionario == "Gerente"
        ):
            print("Acesso autorizado.")
            return True

    print("Acesso negado. ID, senha ou cargo inválido.")
    return False


# ============================================================
# LISTAGEM
# ============================================================

def listar_funcionarios_resumido(lista_funcionarios):
    """Exibe uma listagem curta de funcionários."""
    if not lista_funcionarios:
        print("\nNenhum funcionário cadastrado.")
        return

    print("\n" + "-" * 80)
    print(f"{'ID':<6} {'Nome':<30} {'Cargo':<15} {'R$/Hora':<12}")
    print("-" * 80)

    for funcionario in lista_funcionarios:
        print(
            f"{funcionario.get('id_funcionario'):<6} "
            f"{funcionario.get('nome', ''):<30} "
            f"{funcionario.get('cargo', ''):<15} "
            f"{funcionario.get('salario_por_hora', 0):<12.2f}"
        )

    print("-" * 80)


def listar_funcionarios_completo(lista_funcionarios):
    """Exibe todos os dados principais dos funcionários."""
    if not lista_funcionarios:
        print("\nNenhum funcionário cadastrado.")
        return

    print("\n" + "=" * 110)
    print("FUNCIONÁRIOS CADASTRADOS")
    print("=" * 110)

    for funcionario in lista_funcionarios:
        print(f"ID: {funcionario.get('id_funcionario')}")
        print(f"Nome: {funcionario.get('nome')}")
        print(f"Cargo: {funcionario.get('cargo')}")
        print(f"Carga Horária: {funcionario.get('carga_horaria')}")
        print(f"Horas Mensais: {funcionario.get('horas_mensais')}")
        print(f"Salário Líquido: R$ {funcionario.get('salario_liquido', 0):.2f}")
        print(f"Salário por Hora: R$ {funcionario.get('salario_por_hora', 0):.2f}")
        print(f"Senha: {funcionario.get('senha')}")
        print("-" * 110)


# ============================================================
# CADASTRO
# ============================================================

def cadastrar_funcionario(lista_funcionarios):
    """Cadastra um novo funcionário."""
    print("\n" + "=" * 60)
    print("REGISTRO DE FUNCIONÁRIO")
    print("=" * 60)

    nome = input("Digite o nome do funcionário: ").strip()
    if not nome:
        print("O nome não pode ficar vazio.")
        return lista_funcionarios

    print("\nEscolha o cargo:")
    for codigo, cargo in CARGOS:
        print(f"{codigo} - {cargo}")

    opcao_cargo = input("Digite a opção do cargo: ").strip()
    cargo = obter_cargo_por_opcao(opcao_cargo)

    if not cargo:
        print("Favor, digite uma opção válida")
        return lista_funcionarios

    if cargo == "Gerente" and existe_gerente(lista_funcionarios):
        print("Já existe um gerente cadastrado no sistema.")
        return lista_funcionarios

    salario_digitado = input("Digite o salário líquido do funcionário: ").replace(",", ".").strip()
    try:
        salario_liquido = float(salario_digitado)
    except ValueError:
        print("Salário inválido.")
        return lista_funcionarios

    print("\nModelos de carga horária:")
    cargas_horarias = tuple(MAPEAMENTO_CARGA_HORARIA.keys())

    for indice, carga_horaria in enumerate(cargas_horarias, start=1):
        print(f"{indice} - {carga_horaria}")

    opcao_carga = input("Digite a opção da carga horária: ").strip()

    try:
        indice_carga = int(opcao_carga) - 1
        carga_horaria = cargas_horarias[indice_carga]
    except (ValueError, IndexError):
        print("Favor, digite uma opção válida")
        return lista_funcionarios

    horas_mensais = obter_horas_mensais_por_carga(carga_horaria)
    salario_por_hora = round(salario_liquido / horas_mensais, 2)
    novo_id = gerar_novo_id_funcionario(lista_funcionarios)
    senha = gerar_senha_padrao(nome, novo_id)

    novo_funcionario = {
        "id_funcionario": novo_id,
        "senha": senha,
        "nome": nome,
        "cargo": cargo,
        "salario_liquido": salario_liquido,
        "carga_horaria": carga_horaria,
        "horas_mensais": horas_mensais,
        "salario_por_hora": salario_por_hora,
        "ativo": True,
        "data_cadastro": obter_data_atual(),
    }

    lista_funcionarios.append(novo_funcionario)
    salvar_funcionarios(lista_funcionarios)

    print("\nFuncionário cadastrado com sucesso.")
    print(f"ID: {novo_id}")
    print(f"Senha gerada: {senha}")
    print(f"Salário por hora: R$ {salario_por_hora:.2f}")

    return lista_funcionarios
