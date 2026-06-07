from utils import carregar_dados, salvar_dados

ARQUIVO_COMPUTADORES = "computadores.json"


def carregar_computadores():
    """Carrega computadores do JSON."""
    return carregar_dados(ARQUIVO_COMPUTADORES)


def salvar_computadores(lista_computadores):
    """Salva computadores no JSON."""
    return salvar_dados(lista_computadores, ARQUIVO_COMPUTADORES)


def gerar_novo_id(lista_computadores):
    """Gera o próximo ID de computador."""
    if not lista_computadores:
        return 1

    ids_existentes = []
    for computador in lista_computadores:
        ids_existentes.append(computador.get("id", 0))

    return max(ids_existentes) + 1


def buscar_computador_id(lista_computadores, id_computador):
    """Busca computador por ID."""
    for computador in lista_computadores:
        if computador.get("id") == id_computador:
            return computador

    return None
