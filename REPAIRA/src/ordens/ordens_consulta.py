def listar_ordens_abertas(lista_ordens, lista_computadores=None):
    """Lista ordens abertas ou em andamento."""
    ordens_ativas = []

    for ordem in lista_ordens:
        if ordem.get("status") in ["Aberta", "Em Andamento"]:
            ordens_ativas.append(ordem)

    if not ordens_ativas:
        print("\nNenhuma ordem aberta ou em andamento.")
        return

    print("\n" + "=" * 125)
    print("ORDENS ABERTAS / EM ANDAMENTO")
    print("=" * 125)
    print(
        f"{'OS':<5} {'Computador':<18} {'Tipo':<12} "
        f"{'Prioridade':<10} {'Funcionário':<25} {'Status':<15} {'SLA':<12}"
    )
    print("-" * 125)

    for ordem in ordens_ativas:
        print(
            f"{ordem.get('id_os'):<5} "
            f"{ordem.get('nome_computador', ''):<18} "
            f"{ordem.get('tipo_manutencao', ''):<12} "
            f"{ordem.get('prioridade', ''):<10} "
            f"{ordem.get('nome_funcionario', ''):<25} "
            f"{ordem.get('status', ''):<15} "
            f"{ordem.get('sla_previsto', ''):<12}"
        )


def listar_ordens_por_funcionario(lista_ordens, lista_funcionarios):
    """Lista quantidade de ordens por funcionário."""
    if not lista_funcionarios:
        print("Nenhum funcionário cadastrado.")
        return

    print("\nORDENS POR FUNCIONÁRIO")
    print("=" * 80)

    for funcionario in lista_funcionarios:
        ordens_do_funcionario = []

        for ordem in lista_ordens:
            if ordem.get("id_funcionario") == funcionario.get("id_funcionario"):
                ordens_do_funcionario.append(ordem)

        if not ordens_do_funcionario:
            continue

        ordens_pendentes = []
        ordens_concluidas = []

        for ordem in ordens_do_funcionario:
            if ordem.get("status") in ["Aberta", "Em Andamento"]:
                ordens_pendentes.append(ordem)
            elif ordem.get("status") == "Concluída":
                ordens_concluidas.append(ordem)

        print(
            f"{funcionario.get('nome')} | "
            f"Total: {len(ordens_do_funcionario)} | "
            f"Pendentes: {len(ordens_pendentes)} | "
            f"Concluídas: {len(ordens_concluidas)}"
        )
