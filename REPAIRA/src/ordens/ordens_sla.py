from datetime import datetime, timedelta


def calcular_sla(prioridade):
    """Calcula a data prevista de SLA pela prioridade."""
    dias_por_prioridade = {
        "Crítica": 1,
        "Alta": 2,
        "Média": 5,
        "Baixa": 10,
    }

    dias = dias_por_prioridade.get(prioridade, 10)
    data_sla = datetime.now() + timedelta(days=dias)

    return data_sla.strftime("%Y-%m-%d")


def verificar_sla_atraso(lista_ordens):
    """Exibe ordens atrasadas ou próximas do vencimento."""
    if not lista_ordens:
        print("\nNenhuma ordem cadastrada.")
        return

    data_hoje = datetime.now().date()
    encontrou_alerta = False

    print("\n" + "=" * 70)
    print("VERIFICAÇÃO DE SLA")
    print("=" * 70)

    for ordem in lista_ordens:
        status_ordem = ordem.get("status")

        if status_ordem not in ["Aberta", "Em Andamento"]:
            continue

        data_sla = datetime.strptime(ordem.get("sla_previsto"), "%Y-%m-%d").date()
        dias_restantes = (data_sla - data_hoje).days

        if dias_restantes < 0:
            print(f"ATRASADA | OS {ordem.get('id_os')} | {abs(dias_restantes)} dia(s)")
            encontrou_alerta = True
        elif dias_restantes <= 2:
            print(f"PRÓXIMA | OS {ordem.get('id_os')} | {dias_restantes} dia(s)")
            encontrou_alerta = True

    if not encontrou_alerta:
        print("Nenhum alerta de SLA encontrado.")
