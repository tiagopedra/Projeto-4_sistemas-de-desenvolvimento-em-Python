from computadores import (
    carregar_computadores,
    cadastrar_computador,
    listar_computadores,
    atualizar_status_computador,
    deletar_computador,
)
from ordens import (
    carregar_ordens,
    criar_ordem,
    listar_ordens_abertas,
    atualizar_status_ordem,
    verificar_sla_atraso,
    listar_ordens_por_funcionario,
)
from historico import (
    exibir_historico_completo,
    exibir_historico_por_computador,
    exibir_estatisticas,
    exibir_sla_alerta,
)
from funcionarios import (
    carregar_funcionarios,
    cadastrar_funcionario,
    listar_funcionarios_completo,
    autenticar_gerente,
)
from monetario import menu_consulta_monetaria


# ============================================================
# MENUS
# ============================================================

def exibir_menu_principal():
    """Exibe o menu principal do sistema."""
    print("\n" + "=" * 50)
    print(" SISTEMA DE MANUTENÇÃO DE COMPUTADORES")
    print("=" * 50)
    print("[1] Gerenciar Computadores")
    print("[2] Gerenciar Ordens de Serviço")
    print("[3] Histórico e Estatísticas")
    print("[4] Registrar Funcionários")
    print("[5] Consulta Monetária")
    print("[0] Sair")
    print("=" * 50)


def exibir_menu_computadores():
    """Exibe o submenu de computadores."""
    print("\n--- GERENCIAR COMPUTADORES ---")
    print("[1] Cadastrar computador")
    print("[2] Listar computadores")
    print("[3] Atualizar status")
    print("[4] Deletar computador")
    print("[0] Voltar")


def exibir_menu_ordens():
    """Exibe o submenu de ordens de serviço."""
    print("\n--- GERENCIAR ORDENS DE SERVIÇO ---")
    print("[1] Abrir nova ordem")
    print("[2] Listar ordens abertas")
    print("[3] Atualizar/Fechar ordem")
    print("[4] Verificar SLA")
    print("[5] Listar ordens por funcionário")
    print("[0] Voltar")


def exibir_menu_historico():
    """Exibe o submenu de histórico."""
    print("\n--- HISTÓRICO E ESTATÍSTICAS ---")
    print("[1] Histórico completo")
    print("[2] Histórico por computador")
    print("[3] Estatísticas gerais")
    print("[4] Alertas de SLA")
    print("[0] Voltar")


def exibir_menu_funcionarios():
    """Exibe o submenu de funcionários."""
    print("\n--- REGISTRAR FUNCIONÁRIOS ---")
    print("[1] Cadastrar funcionário")
    print("[2] Listar funcionários")
    print("[0] Voltar")


# ============================================================
# FLUXOS DE MENU
# ============================================================

def menu_computadores(computadores):
    """Controla o submenu de computadores."""
    while True:
        exibir_menu_computadores()
        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            computadores = cadastrar_computador(computadores)
        elif opcao == "2":
            listar_computadores(computadores)
        elif opcao == "3":
            computadores = atualizar_status_computador(computadores)
        elif opcao == "4":
            computadores = deletar_computador(computadores)
        elif opcao == "0":
            return computadores
        else:
            print("Opção inválida.")


def menu_ordens(ordens, computadores, funcionarios):
    """Controla o submenu de ordens de serviço."""
    while True:
        exibir_menu_ordens()
        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            ordens = criar_ordem(ordens, computadores, funcionarios)
        elif opcao == "2":
            listar_ordens_abertas(ordens, computadores)
        elif opcao == "3":
            # Importante: esta função precisa da lista de funcionários,
            # pois o fechamento da OS calcula o custo pelo salário por hora.
            ordens = atualizar_status_ordem(ordens, funcionarios)
        elif opcao == "4":
            verificar_sla_atraso(ordens)
        elif opcao == "5":
            listar_ordens_por_funcionario(ordens, funcionarios)
        elif opcao == "0":
            return ordens
        else:
            print("Opção inválida.")


def menu_historico(ordens, computadores):
    """Controla o submenu de histórico e estatísticas."""
    while True:
        exibir_menu_historico()
        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            exibir_historico_completo(ordens)
        elif opcao == "2":
            exibir_historico_por_computador(ordens, computadores)
        elif opcao == "3":
            exibir_estatisticas(ordens, computadores)
        elif opcao == "4":
            exibir_sla_alerta(ordens)
        elif opcao == "0":
            return
        else:
            print("Opção inválida.")


def menu_funcionarios(funcionarios):
    """Controla o submenu de funcionários."""
    while True:
        exibir_menu_funcionarios()
        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            funcionarios = cadastrar_funcionario(funcionarios)
        elif opcao == "2":
            listar_funcionarios_completo(funcionarios)
        elif opcao == "0":
            return funcionarios
        else:
            print("Opção inválida.")


# ============================================================
# PROGRAMA PRINCIPAL
# ============================================================

def main():
    """Função principal do sistema."""
    computadores = carregar_computadores()
    ordens = carregar_ordens()
    funcionarios = carregar_funcionarios()

    while True:
        exibir_menu_principal()
        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            computadores = menu_computadores(computadores)

        elif opcao == "2":
            ordens = menu_ordens(ordens, computadores, funcionarios)

        elif opcao == "3":
            menu_historico(ordens, computadores)

        elif opcao == "4":
            if autenticar_gerente():
                funcionarios = carregar_funcionarios()
                funcionarios = menu_funcionarios(funcionarios)

        elif opcao == "5":
            if autenticar_gerente():
                # Recarrega os dados antes da consulta para garantir persistência atualizada.
                funcionarios = carregar_funcionarios()
                ordens = carregar_ordens()
                menu_consulta_monetaria(ordens, funcionarios)

        elif opcao == "0":
            print("\nSaindo do sistema...")
            break

        else:
            print("Opção inválida.")


if __name__ == "__main__":
    main()
