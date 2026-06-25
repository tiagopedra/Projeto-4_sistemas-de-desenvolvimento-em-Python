from dados import cadastrar_clientes, alterar_status
from relatorio import listar_clientes, pesquisar_chamado, relatorio_financeiro
from acoes import lancar_tecnico, excluir_chamado
import storage


class Empresa:
    # listar, pesquisar, cadastrar, alterar status, excluir chamado, enviar técnico
    # decomposição: as funções ficam separadas em dados.py, relatorio.py e acoes.py

    def __init__(self):
        storage.init_db()
        self.clientes = []
        self.indice = {}

        # Carrega os clientes salvos no banco de dados SQLite.
        rows = storage.load_all_clients()
        max_chamado = 0
        from cliente import Cliente

        for r in rows:
            cliente = Cliente(
                r.get("nome"),
                r.get("chamado"),
                r.get("problema"),
                r.get("cpf"),
                r.get("contato"),
                r.get("tipo_problema"),
                r.get("prazo_resolucao"),
                r.get("valor_manutencao"),
                r.get("peca"),
                r.get("quantidade_peca"),
                r.get("valor_peca"),
                r.get("forma_pagamento"),
                r.get("status_pagamento"),
                r.get("observacao_financeira"),
            )
            cliente.tecnico = r.get("tecnico")
            cliente.status = r.get("status") or cliente.status
            self.clientes.append(cliente)
            self.indice[cliente.chamado] = cliente

            if cliente.chamado and cliente.chamado > max_chamado:
                max_chamado = cliente.chamado

        self.proximo_chamado = max_chamado + 1 if max_chamado > 0 else 1

    def cadastrar_clientes(self):
        cadastrar_clientes(self)

    def alterar_status(self):
        alterar_status(self)

    def listar_clientes(self):
        listar_clientes(self)

    def pesquisar_chamado(self):
        pesquisar_chamado(self)

    def relatorio_financeiro(self):
        relatorio_financeiro(self)

    def lancar_tecnico(self):
        lancar_tecnico(self)

    def excluir_chamado(self):
        excluir_chamado(self)
