from datetime import datetime
from computadores import buscar_computador_id


def exibir_historico_completo(lista_ordens):
    """Exibe todas as ordens concluídas."""
    ordens_concluidas = []

    for ordem in lista_ordens:
        if ordem.get("status") == "Concluída":
            ordens_concluidas.append(ordem)

    if not ordens_concluidas:
        print("\nNenhuma ordem concluída ainda.")
        return

    print("\nHISTÓRICO DE MANUTENÇÕES")
    print("=" * 100)

    for ordem in ordens_concluidas:
        print(
            f"OS {ordem.get('id_os')} | "
            f"{ordem.get('nome_computador')} | "
            f"{ordem.get('tipo_manutencao')} | "
            f"{ordem.get('data_conclusao')}"
        )


def exibir_historico_por_computador(lista_ordens, lista_computadores):
    """Exibe histórico por computador."""
    for computador in lista_computadores:
        print(f"ID: {computador.get('id')} - {computador.get('nome')}")

    try:
        id_computador = int(input("\nDigite o ID do computador: ").strip())
    except ValueError:
        print("ID inválido.")
        return

    computador = buscar_computador_id(lista_computadores, id_computador)

    if not computador:
        print("Computador não encontrado.")
        return

    ordens_do_computador = []

    for ordem in lista_ordens:
        if ordem.get("id_computador") == id_computador:
            ordens_do_computador.append(ordem)

    if not ordens_do_computador:
        print("Nenhuma OS para este computador.")
        return

    for ordem in ordens_do_computador:
        print(
            f"OS {ordem.get('id_os')} | "
            f"{ordem.get('tipo_manutencao')} | "
            f"{ordem.get('status')} | "
            f"{ordem.get('data_abertura')}"
        )


def exibir_estatisticas(lista_ordens, lista_computadores):
    """Exibe estatísticas gerais."""
    total_ordens = len(lista_ordens)
    total_computadores = len(lista_computadores)

    ordens_ativas = []
    ordens_concluidas = []

    for ordem in lista_ordens:
        if ordem.get("status") in ["Aberta", "Em Andamento"]:
            ordens_ativas.append(ordem)
        elif ordem.get("status") == "Concluída":
            ordens_concluidas.append(ordem)

    print("\nESTATÍSTICAS")
    print("=" * 60)
    print(f"Total de computadores: {total_computadores}")
    print(f"Total de OS: {total_ordens}")
    print(f"Abertas/Em andamento: {len(ordens_ativas)}")
    print(f"Concluídas: {len(ordens_concluidas)}")


def exibir_sla_alerta(lista_ordens):
    """Exibe alertas de SLA."""
    data_hoje = datetime.now().date()
    encontrou_alerta = False

    for ordem in lista_ordens:
        if ordem.get("status") not in ["Aberta", "Em Andamento"]:
            continue

        data_sla = datetime.strptime(ordem.get("sla_previsto"), "%Y-%m-%d").date()
        dias_restantes = (data_sla - data_hoje).days

        if dias_restantes <= 2:
            print(
                f"OS {ordem.get('id_os')} | "
                f"SLA {ordem.get('sla_previsto')} | "
                f"Dias restantes: {dias_restantes}"
            )
            encontrou_alerta = True

    if not encontrou_alerta:
        print("Nenhum alerta de SLA.")
