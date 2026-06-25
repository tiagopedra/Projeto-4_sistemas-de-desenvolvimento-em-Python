from cliente import Cliente
import storage


PROBLEMAS = (
    (1, "O computador não conecta na internet", "Até 1 dia útil"),
    (2, "O computador não liga", "Até 2 dias úteis"),
    (3, "Problemas com periféricos", "Até 1 dia útil"),
    (4, "Problemas com monitor", "Até 2 dias úteis"),
    (5, "Outros/Problemas diversos", "Prazo definido após avaliação técnica"),
)

STATUS_PAGAMENTO = (
    (1, "Aguardando orçamento"),
    (2, "Pendente"),
    (3, "Pago"),
    (4, "Cancelado"),
)


def cadastrar_clientes(self):
    while True:
        nome = input("Digite o nome do cliente: ")
        if nome.replace(" ", "").isalpha():
            break
        else:
            print("\nNome inválido. Digite apenas letras.\n")

    while True:
        try:
            cpf = int(input("Digite o CPF do cliente (somente números): "))
            break
        except ValueError:
            print("\nDigite apenas números para o CPF.\n")

    while True:
        try:
            contato = int(input("Digite o número de contato do cliente (somente números): "))
            break
        except ValueError:
            print("\nDigite apenas números para o contato.\n")

    chamado = self.proximo_chamado
    self.proximo_chamado += 1

    print(f"\nChamado gerado automaticamente: {chamado}\n")
    print("\nEscolha seu problema: ")
    for numero, descricao, prazo in PROBLEMAS:
        print(f"{numero} - {descricao} | Prazo: {prazo}")

    while True:
        try:
            opc_problema = int(input("Escolha uma opção de 1 a 5:  "))
            if 1 <= opc_problema <= 5:
                break
            else:
                print("Opção inválida. Digite um número de 1 a 5.")
        except ValueError:
            print("Erro: digite apenas números de 1 a 5.")

    match opc_problema:
        case 1 | 2 | 3 | 4:
            descricao = PROBLEMAS[opc_problema - 1][1]
            prazo_resolucao = PROBLEMAS[opc_problema - 1][2]
            problema = f"{opc_problema} - {descricao}"
            tipo_problema = "conhecido"
        case 5:
            problema = input("Descreva o problema: ")
            prazo_resolucao = PROBLEMAS[opc_problema - 1][2]
            tipo_problema = "desconhecido"
        case _:
            print("Opção inválida.")
            return

    print(f"\nPrazo estimado para resolução: {prazo_resolucao}")
    print("\nINFORMAÇÕES FINANCEIRAS DO CHAMADO")

    while True:
        try:
            valor_manutencao = float(input("Digite o valor da manutenção: R$ ").replace(",", "."))
            break
        except ValueError:
            print("\nDigite apenas números para o valor da manutenção.\n")

    peca = input("Digite a peça utilizada (caso não tenha, digite 'Nenhuma'): ")

    while True:
        try:
            quantidade_peca = int(input("Digite a quantidade de peças utilizadas: "))
            break
        except ValueError:
            print("\nDigite apenas números para a quantidade de peças.\n")

    while True:
        try:
            valor_peca = float(input("Digite o valor da peça: R$ ").replace(",", "."))
            break
        except ValueError:
            print("\nDigite apenas números para o valor da peça.\n")

    forma_pagamento = input("Digite a forma de pagamento: ")

    print("\nEscolha o status do pagamento:")
    for numero, status in STATUS_PAGAMENTO:
        print(f"{numero}. {status}")

    while True:
        try:
            opc_pagamento = int(input("Escolha uma opção de 1 a 4: "))
            if 1 <= opc_pagamento <= 4:
                break
            else:
                print("Opção inválida. Digite um número de 1 a 4.")
        except ValueError:
            print("Erro: digite apenas números de 1 a 4.")

    match opc_pagamento:
        case 1 | 2 | 3 | 4:
            status_pagamento = STATUS_PAGAMENTO[opc_pagamento - 1][1]
        case _:
            print("Opção inválida.")
            return

    observacao_financeira = input("Digite uma observação financeira: ")

    cliente = Cliente(
        nome,
        chamado,
        problema,
        cpf,
        contato,
        tipo_problema,
        prazo_resolucao,
        valor_manutencao,
        peca,
        quantidade_peca,
        valor_peca,
        forma_pagamento,
        status_pagamento,
        observacao_financeira,
    )
    self.clientes.append(cliente)
    # manter índice para acesso O(1) por chamado
    try:
        self.indice[chamado] = cliente
    except Exception:
        pass

    # persistir no banco
    try:
        storage.insert_cliente(cliente)
    except Exception:
        # falha no DB não deve quebrar fluxo interativo
        print("Aviso: não foi possível salvar o chamado no banco de dados.")

    print("\nCliente e problema cadastrado com sucesso, enviaremos um técnico especializado para o problema solicitado")


def alterar_status(self):
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
        # índice pode não existir em versões antigas; fallback para busca linear
        for c in self.clientes:
            if c.chamado == chamado:
                cliente = c
                break

    if cliente is None:
        print(f"\nChamado {chamado} não encontrado.")
        return

    print("\nEscolha o novo status:")
    print("1. Problema solucionado")
    print("2. Arquivar")
    print("3. Indefinido")
    print("0. Voltar")

    while True:
        try:
            opc = int(input("Escolha uma opção: "))

            match opc:
                case 1:
                    cliente.status = "Problema solucionado"
                    print("\nStatus alterado para 'Problema solucionado'.")
                    try:
                        storage.update_cliente(chamado, status=cliente.status)
                    except Exception:
                        pass
                case 2:
                    cliente.status = "Chamado Arquivado"
                    print("\nChamado arquivado.")
                    try:
                        storage.update_cliente(chamado, status=cliente.status)
                    except Exception:
                        pass
                case 3:
                    cliente.status = "Chamado Indefinido"
                    print("\nChamado Indefinido Novamente.")
                    try:
                        storage.update_cliente(chamado, status=cliente.status)
                    except Exception:
                        pass
                case 0:
                    break
                case _:
                    print("Opção inválida.")
                    continue
            break
        except ValueError:
            print("Digite apenas números.")
    return

    print(f"\nChamado {chamado} não encontrado.")
