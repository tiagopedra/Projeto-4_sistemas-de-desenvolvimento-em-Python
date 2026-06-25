class Cliente:

    def __init__(self, nome, chamado, problema, cpf, contato, tipo_problema, prazo_resolucao, valor_manutencao, peca, quantidade_peca, valor_peca, forma_pagamento, status_pagamento, observacao_financeira):
        self.nome = nome
        self.chamado = chamado
        self.problema = problema
        self.cpf = cpf
        self.contato = contato
        self.tecnico = None
        self.status = "Indefinido"
        self.tipo_problema = tipo_problema
        self.prazo_resolucao = prazo_resolucao
        self.valor_manutencao = valor_manutencao
        self.peca = peca
        self.quantidade_peca = quantidade_peca
        self.valor_peca = valor_peca
        self.forma_pagamento = forma_pagamento
        self.status_pagamento = status_pagamento
        self.observacao_financeira = observacao_financeira

    def exibir_dados(self):
        print("\nDADOS DO CLIENTE")
        print("Nome:", self.nome)
        print("CPF:", self.cpf)
        print("Contato:", self.contato)
        print("Chamado:", self.chamado)
        print("Problema:", self.problema)
        print("Tipo de problema:", self.tipo_problema)
        print("Prazo estimado de resolução:", self.prazo_resolucao)
        print("Status:", self.status)
        print("Valor da manutenção: R$", self.valor_manutencao)
        print("Peça utilizada:", self.peca)
        print("Quantidade de peças:", self.quantidade_peca)
        print("Valor da peça: R$", self.valor_peca)
        print("Forma de pagamento:", self.forma_pagamento)
        print("Status do pagamento:", self.status_pagamento)
        print("Observação financeira:", self.observacao_financeira)
