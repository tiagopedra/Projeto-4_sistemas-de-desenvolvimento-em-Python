from utils import obter_data_atual
from .computadores_repo import gerar_novo_id, salvar_computadores


def cadastrar_computador(lista_computadores):
    """Cadastra um novo computador."""
    print("\n" + "=" * 50)
    print("CADASTRO DE NOVO COMPUTADOR")
    print("=" * 50)

    nome = input("Digite o nome do computador: ").strip()
    tipo = input("Tipo (Desktop/Notebook/All-in-One): ").strip()
    modelo = input("Modelo: ").strip()
    processador = input("Processador: ").strip()
    memoria_ram = input("Memória RAM: ").strip()
    armazenamento = input("Armazenamento: ").strip()
    sistema_operacional = input("Sistema Operacional: ").strip()
    localizacao = input("Localização: ").strip()
    departamento = input("Departamento: ").strip()

    novo_id = gerar_novo_id(lista_computadores)

    novo_computador = {
        "id": novo_id,
        "nome": nome,
        "tipo": tipo,
        "modelo": modelo,
        "processador": processador,
        "memoria_ram": memoria_ram,
        "armazenamento": armazenamento,
        "sistema_operacional": sistema_operacional,
        "localizacao": localizacao,
        "departamento": departamento,
        "status": "Operacional",
        "data_cadastro": obter_data_atual(),
        "ultima_manutencao": None,
    }

    lista_computadores.append(novo_computador)
    salvar_computadores(lista_computadores)

    print("\nComputador cadastrado com sucesso.")
    print(f"ID: {novo_id}")
    print(f"Nome: {nome}")

    return lista_computadores
