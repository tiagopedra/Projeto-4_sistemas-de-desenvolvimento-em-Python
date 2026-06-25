def listar_clientes(self):
    if len(self.clientes) == 0:
        print("\nNenhum cliente cadastrado.")
        return

    print("\nLISTA DE CLIENTES ATIVOS")
    for cliente in self.clientes:
        print(f"Chamado: {cliente.chamado} | Nome: {cliente.nome} | Status: {cliente.status}")

    total_clientes = len(self.clientes)
    print(f"\nTotal de clientes cadastrados: {total_clientes}")


def pesquisar_chamado(self):
    if len(self.clientes) == 0:
        print("\nNenhum cliente cadastrado.")
        return

    while True:
        try:
            chamado = int(input("Digite o número do chamado: "))
            break
        except ValueError:
            print("\nDigite apenas números.\n")

    cliente = None
    try:
        cliente = self.indice.get(chamado)
    except Exception:
        for c in self.clientes:
            if c.chamado == chamado:
                cliente = c
                break

    if cliente:
        cliente.exibir_dados()
        return

    print(f"\nChamado {chamado} não encontrado.")


def relatorio_financeiro(self):
    if len(self.clientes) == 0:
        print("\nNenhum cliente cadastrado.")
        return

    total_manutencao = 0
    total_pecas = 0
    total_geral = 0
    total_pago = 0
    total_pendente = 0
    total_aguardando_orcamento = 0
    total_cancelado = 0

    qtd_pagos = 0
    qtd_pendentes = 0
    qtd_aguardando = 0
    qtd_cancelados = 0

    print("\nRELATÓRIO FINANCEIRO")
    print("-" * 50)

    for cliente in self.clientes:
        valor_manutencao = float(cliente.valor_manutencao or 0)
        valor_pecas = float(cliente.valor_peca or 0) * int(cliente.quantidade_peca or 0)
        total_chamado = valor_manutencao + valor_pecas

        total_manutencao += valor_manutencao
        total_pecas += valor_pecas
        total_geral += total_chamado

        status_pagamento = str(cliente.status_pagamento or "").casefold()

        if status_pagamento == "pago":
            total_pago += total_chamado
            qtd_pagos += 1
        elif status_pagamento == "pendente":
            total_pendente += total_chamado
            qtd_pendentes += 1
        elif status_pagamento == "aguardando orçamento":
            total_aguardando_orcamento += total_chamado
            qtd_aguardando += 1
        elif status_pagamento == "cancelado":
            total_cancelado += total_chamado
            qtd_cancelados += 1

    print(f"Total em manutenções: R$ {total_manutencao:.2f}")
    print(f"Total em peças: R$ {total_pecas:.2f}")
    print(f"Valor total dos chamados: R$ {total_geral:.2f}")
    print("-" * 50)
    print(f"Total pago: R$ {total_pago:.2f} | Quantidade: {qtd_pagos}")
    print(f"Total pendente: R$ {total_pendente:.2f} | Quantidade: {qtd_pendentes}")
    print(f"Total aguardando orçamento: R$ {total_aguardando_orcamento:.2f} | Quantidade: {qtd_aguardando}")
    print(f"Total cancelado: R$ {total_cancelado:.2f} | Quantidade: {qtd_cancelados}")
    print("-" * 50)
    print(f"Total de chamados analisados: {len(self.clientes)}")
