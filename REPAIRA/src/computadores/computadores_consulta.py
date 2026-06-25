def listar_computadores(lista_computadores):
    """Lista todos os computadores cadastrados."""
    if not lista_computadores:
        print("\nNão há computadores cadastrados.")
        return

    print("\n" + "=" * 100)
    print("INVENTÁRIO DE COMPUTADORES")
    print("=" * 100)
    print(f"{'ID':<5} {'Nome':<22} {'Modelo':<24} {'Status':<16} {'Localização':<22}")
    print("-" * 100)

    for computador in lista_computadores:
        print(
            f"{computador.get('id'):<5} "
            f"{computador.get('nome', ''):<22} "
            f"{computador.get('modelo', ''):<24} "
            f"{computador.get('status', ''):<16} "
            f"{computador.get('localizacao', ''):<22}"
        )

    print("=" * 100)
    print(f"Total de computadores: {len(lista_computadores)}")


def listar_computadores_resumido(lista_computadores):
    """Lista computadores com ID, nome e status."""
    if not lista_computadores:
        print("Nenhum computador cadastrado.")
        return

    print("\n" + "-" * 60)
    print(f"{'ID':<5} {'Nome':<25} {'Status':<15}")
    print("-" * 60)

    for computador in lista_computadores:
        print(
            f"{computador.get('id'):<5} "
            f"{computador.get('nome', ''):<25} "
            f"{computador.get('status', ''):<15}"
        )


def exibir_detalhes_computador(computador):
    """Exibe detalhes de um computador."""
    print("\n" + "=" * 60)
    print(f"DETALHES DO COMPUTADOR - ID: {computador.get('id')}")
    print("=" * 60)

    for chave, valor in computador.items():
        print(f"{chave}: {valor}")
