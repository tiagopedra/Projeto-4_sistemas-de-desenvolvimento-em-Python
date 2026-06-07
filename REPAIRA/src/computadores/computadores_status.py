from utils import obter_data_atual
from .computadores_repo import buscar_computador_id, salvar_computadores
from .computadores_consulta import listar_computadores_resumido


def atualizar_status_computador(lista_computadores):
    """Atualiza o status de um computador."""
    if not lista_computadores:
        print("\nNenhum computador cadastrado.")
        return lista_computadores

    listar_computadores_resumido(lista_computadores)

    try:
        id_computador = int(input("\nDigite o ID do computador: ").strip())
    except ValueError:
        print("ID inválido.")
        return lista_computadores

    computador = buscar_computador_id(lista_computadores, id_computador)

    if not computador:
        print("Computador não encontrado.")
        return lista_computadores

    print("\nNovo status:")
    print("1 - Operacional")
    print("2 - Em Manutenção")
    print("3 - Inativo")

    status_por_opcao = {
        "1": "Operacional",
        "2": "Em Manutenção",
        "3": "Inativo",
    }

    opcao_status = input("Escolha uma opção: ").strip()
    novo_status = status_por_opcao.get(opcao_status)

    if not novo_status:
        print("Opção inválida.")
        return lista_computadores

    computador["status"] = novo_status

    if novo_status == "Em Manutenção":
        computador["ultima_manutencao"] = obter_data_atual()

    salvar_computadores(lista_computadores)
    print("Status atualizado com sucesso.")

    return lista_computadores


def deletar_computador(lista_computadores):
    """Remove um computador após confirmação."""
    if not lista_computadores:
        print("\nNenhum computador cadastrado.")
        return lista_computadores

    listar_computadores_resumido(lista_computadores)

    try:
        id_computador = int(input("\nDigite o ID do computador a deletar: ").strip())
    except ValueError:
        print("ID inválido.")
        return lista_computadores

    computador = buscar_computador_id(lista_computadores, id_computador)

    if not computador:
        print("Computador não encontrado.")
        return lista_computadores

    confirmacao = input("Digite SIM para confirmar: ").strip().upper()

    if confirmacao == "SIM":
        lista_computadores.remove(computador)
        salvar_computadores(lista_computadores)
        print("Computador removido com sucesso.")
    else:
        print("Operação cancelada.")

    return lista_computadores
