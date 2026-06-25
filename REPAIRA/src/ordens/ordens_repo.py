from utils import carregar_dados, salvar_dados

ARQUIVO_ORDENS = "ordem_servico.json"


def carregar_ordens():
    """Carrega ordens de serviço do JSON."""
    return carregar_dados(ARQUIVO_ORDENS)


def salvar_ordens(lista_ordens):
    """Salva ordens de serviço no JSON."""
    return salvar_dados(lista_ordens, ARQUIVO_ORDENS)


def gerar_novo_id_os(lista_ordens):
    """Gera o próximo ID de ordem de serviço."""
    if not lista_ordens:
        return 1

    ids_existentes = []
    for ordem in lista_ordens:
        ids_existentes.append(ordem.get("id_os", 0))

    return max(ids_existentes) + 1
