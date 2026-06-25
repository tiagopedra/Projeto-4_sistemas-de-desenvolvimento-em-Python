import storage


def lancar_tecnico(self):
    if not self.clientes:
        print("\nNenhum cliente cadastrado.")
        return

    while True:
        try:
            chamado = int(input("Digite o número do chamado: "))
            break
        except ValueError:
            print("\nDigite apenas números.\n")

    cliente = self.indice.get(chamado)

    if cliente is None:
        print(f"\nChamado {chamado} não encontrado.")
        return

    if cliente.status == "Técnico enviado":
        print(f"\nAviso: O técnico já está a caminho para o chamado {chamado}!")
        return

    print("\nEnviando técnico...")
    print(f"Cliente: {cliente.nome}")
    print(f"Problema: {cliente.problema}")
    print(f"Prazo estimado de resolução: {cliente.prazo_resolucao}")

    cliente.tecnico = "Técnico enviado"
    cliente.status = "Técnico enviado"

    try:
        storage.update_cliente(
            chamado,
            tecnico=cliente.tecnico,
            status=cliente.status
        )
    except Exception:
        print("\nAviso: não foi possível atualizar o chamado no banco de dados.")

    print("\nTécnico enviado com sucesso.")


def excluir_chamado(self):
    if not self.clientes:
        print("\nNenhum cliente cadastrado.")
        return

    while True:
        try:
            chamado = int(input("Digite o número do chamado a ser excluído: "))
            break
        except ValueError:
            print("\nDigite apenas números.\n")

    cliente = self.indice.get(chamado)

    if cliente is None:
        print(f"\nChamado {chamado} não encontrado.")
        return

    print("\nDados do chamado a ser excluído:")
    cliente.exibir_dados()

    confirmacao = input(
        "\nDeseja realmente excluir este chamado? (SIM/NAO ou S/N): "
    ).strip().upper()

    match confirmacao:
        case "SIM" | "S":
            try:
                self.clientes.remove(cliente)
            except ValueError:
                pass

            try:
                del self.indice[chamado]
            except KeyError:
                pass

            try:
                storage.delete_cliente(chamado)
            except Exception:
                print("\nAviso: não foi possível excluir o chamado do banco de dados.")

            print(f"\nChamado {chamado} excluído com sucesso.")

        case "NAO" | "NÃO" | "N":
            print("\nExclusão cancelada.")

        case _:
            print("\nOpção inválida. Exclusão cancelada.")

    return