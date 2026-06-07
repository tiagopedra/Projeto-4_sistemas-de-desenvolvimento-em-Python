from collections import defaultdict
from funcionarios import buscar_funcionario_id


def recalcular_custo_ordem(ordem, lista_funcionarios):
    """Recalcula o custo de uma OS com base no salário por hora e no tempo gasto."""
    funcionario = buscar_funcionario_id(lista_funcionarios, ordem.get("id_funcionario"))

    if not funcionario:
        return 0.0

    horas_gastas = ordem.get("tempo_total_horas", 0)
    salario_por_hora = funcionario.get("salario_por_hora", 0)

    return round(salario_por_hora * horas_gastas, 2)


def exibir_custo_por_os(lista_ordens, lista_funcionarios):
    """Exibe o custo monetário de cada OS."""
    if not lista_ordens:
        print("\nNenhuma ordem cadastrada.")
        return

    print("\n" + "=" * 120)
    print("CONSULTA MONETÁRIA POR ORDEM DE SERVIÇO")
    print("=" * 120)

    for ordem in lista_ordens:
        custo = recalcular_custo_ordem(ordem, lista_funcionarios)

        print(
            f"OS [{ordem.get('id_os')}] - "
            f"FUNCIONÁRIO [{ordem.get('nome_funcionario')}] "
            f"FUNCIONARIO_ID [{ordem.get('id_funcionario')}] - "
            f"CUSTO R$ {custo:.2f}"
        )


def exibir_total_mensal_por_funcionario(lista_ordens, lista_funcionarios):
    """Exibe o total mensal gasto por funcionário."""
    if not lista_ordens:
        print("\nNenhuma ordem cadastrada.")
        return

    totais_por_funcionario_mes = defaultdict(float)

    for ordem in lista_ordens:
        data_base = (
            ordem.get("data_conclusao")
            or ordem.get("data_inicio_manutencao")
            or ordem.get("data_abertura")
        )

        ano_mes = data_base[:7]
        chave = (
            ordem.get("id_funcionario"),
            ordem.get("nome_funcionario"),
            ano_mes,
        )

        totais_por_funcionario_mes[chave] += recalcular_custo_ordem(
            ordem,
            lista_funcionarios,
        )

    print("\n" + "=" * 120)
    print("TOTAL MENSAL POR FUNCIONÁRIO")
    print("=" * 120)

    itens_ordenados = sorted(
        totais_por_funcionario_mes.items(),
        key=lambda item: (item[0][2], item[0][1]),
    )

    for (id_funcionario, nome_funcionario, ano_mes), valor in itens_ordenados:
        print(
            f"Funcionário {nome_funcionario} "
            f"(ID {id_funcionario}) - {ano_mes} - "
            f"Total em OS: R$ {valor:.2f}"
        )


def exibir_ranking_custos(lista_ordens, lista_funcionarios):
    """Exibe ranking de custo acumulado por funcionário."""
    if not lista_ordens:
        print("\nNenhuma ordem cadastrada.")
        return

    ranking_custos = defaultdict(float)

    for ordem in lista_ordens:
        chave = (
            ordem.get("id_funcionario"),
            ordem.get("nome_funcionario"),
        )

        ranking_custos[chave] += recalcular_custo_ordem(ordem, lista_funcionarios)

    ranking_ordenado = sorted(
        ranking_custos.items(),
        key=lambda item: item[1],
        reverse=True,
    )

    print("\n" + "=" * 90)
    print("RANKING DE CUSTO POR FUNCIONÁRIO")
    print("=" * 90)

    for posicao, ((id_funcionario, nome_funcionario), valor) in enumerate(
        ranking_ordenado,
        start=1,
    ):
        print(
            f"{posicao}º {nome_funcionario} "
            f"(ID {id_funcionario}) - R$ {valor:.2f}"
        )


def menu_consulta_monetaria(lista_ordens, lista_funcionarios):
    """Menu da consulta monetária.

    A autenticação do gerente é feita antes, no main.py.
    """
    while True:
        print("\n" + "=" * 60)
        print("CONSULTA MONETÁRIA")
        print("=" * 60)
        print("[1] Custo por OS")
        print("[2] Total mensal por funcionário")
        print("[3] Ranking de custo")
        print("[0] Voltar")

        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            exibir_custo_por_os(lista_ordens, lista_funcionarios)
        elif opcao == "2":
            exibir_total_mensal_por_funcionario(lista_ordens, lista_funcionarios)
        elif opcao == "3":
            exibir_ranking_custos(lista_ordens, lista_funcionarios)
        elif opcao == "0":
            break
        else:
            print("Opção inválida.")
