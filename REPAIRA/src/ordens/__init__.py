from .ordens_repo import carregar_ordens, salvar_ordens, gerar_novo_id_os
from .ordens_cadastro import criar_ordem
from .ordens_consulta import listar_ordens_abertas, listar_ordens_por_funcionario
from .ordens_status import atualizar_status_ordem
from .ordens_sla import calcular_sla, verificar_sla_atraso
