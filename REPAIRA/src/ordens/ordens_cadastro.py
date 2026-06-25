from utils import obter_data_atual
from computadores import buscar_computador_id
from funcionarios import buscar_funcionario_id, listar_funcionarios_resumido
from .ordens_repo import gerar_novo_id_os, salvar_ordens
from .ordens_sla import calcular_sla

TIPOS_MANUTENCAO = ("Hardware", "Software", "Rede", "Limpeza")
PRIORIDADES = ("Crítica", "Alta", "Média", "Baixa")


def escolher_por_menu(titulo, opcoes):
    """Exibe um menu baseado em tupla e retorna a escolha."""
    print(f"\n{titulo}:")

    for indice, valor in enumerate(opcoes, start=1):
        print(f"[{indice}] {valor}")

    try:
        indice_escolhido = int(input("Escolha uma opção: ").strip()) - 1
        return opcoes[indice_escolhido]
    except (ValueError, IndexError):
        print("Favor, digite uma opção válida")
        return None


def criar_ordem(lista_ordens, lista_computadores, lista_funcionarios):
    """Abre uma nova ordem de serviço.

    A data de abertura e a data de início são automáticas.
    O fechamento, o tempo total e o custo são calculados na atualização da OS.
    """
    print("\n" + "=" * 50)
    print("ABRIR NOVA ORDEM DE SERVIÇO")
    print("=" * 50)

    if not lista_computadores:
        print("Cadastre um computador antes de abrir uma OS.")
        return lista_ordens

    if not lista_funcionarios:
        print("Cadastre um funcionário antes de abrir uma OS.")
        return lista_ordens

    print("\nCOMPUTADORES DISPONÍVEIS:")
    for computador in lista_computadores:
        print(
            f"ID: {computador.get('id')} | "
            f"Nome: {computador.get('nome')} | "
            f"Status: {computador.get('status')}"
        )

    try:
        id_computador = int(input("\nID do computador: ").strip())
    except ValueError:
        print("ID inválido.")
        return lista_ordens

    computador = buscar_computador_id(lista_computadores, id_computador)

    if not computador:
        print("Computador não encontrado.")
        return lista_ordens

    listar_funcionarios_resumido(lista_funcionarios)

    try:
        id_funcionario = int(input("\nID do funcionário responsável: ").strip())
    except ValueError:
        print("ID inválido.")
        return lista_ordens

    funcionario = buscar_funcionario_id(lista_funcionarios, id_funcionario)

    if not funcionario:
        print("Funcionário não encontrado.")
        return lista_ordens

    tipo_manutencao = escolher_por_menu("Tipo de manutenção", TIPOS_MANUTENCAO)
    if not tipo_manutencao:
        return lista_ordens

    descricao = input("Descrição do problema: ").strip()
    if not descricao:
        print("Descrição não pode ficar vazia.")
        return lista_ordens

    prioridade = escolher_por_menu("Prioridade", PRIORIDADES)
    if not prioridade:
        return lista_ordens

    data_abertura = obter_data_atual()
    nome_funcionario = funcionario.get("nome")

    nova_ordem = {
        "id_os": gerar_novo_id_os(lista_ordens),
        "id_computador": computador.get("id"),
        "nome_computador": computador.get("nome"),
        "tipo_manutencao": tipo_manutencao,
        "descricao": descricao,
        "prioridade": prioridade,
        "tecnico_responsavel": nome_funcionario,
        "id_funcionario": funcionario.get("id_funcionario"),
        "nome_funcionario": nome_funcionario,
        "data_abertura": data_abertura,
        "data_inicio_manutencao": data_abertura,
        "data_fim_manutencao": None,
        "tempo_total_horas": 0,
        "status": "Aberta",
        "sla_previsto": calcular_sla(prioridade),
        "data_conclusao": None,
        "solucao_aplicada": None,
        "custo_manutencao": 0,
    }

    lista_ordens.append(nova_ordem)
    salvar_ordens(lista_ordens)

    print(f"\nOS {nova_ordem['id_os']} aberta com sucesso.")
    print(f"Data de abertura: {data_abertura}")

    return lista_ordens
