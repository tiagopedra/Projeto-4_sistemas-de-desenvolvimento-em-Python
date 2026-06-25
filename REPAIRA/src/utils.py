import json
import os
import unicodedata
from datetime import datetime

# Caminho absoluto da pasta src.
# Isso evita erro de persistência quando o projeto é clonado em outra máquina
# ou quando o usuário executa o sistema a partir de diretórios diferentes.
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Caminho absoluto da pasta onde ficam os arquivos JSON.
DADOS_DIR = os.path.join(BASE_DIR, "dados")


# ============================================================
# FUNÇÕES DE PERSISTÊNCIA EM JSON
# ============================================================

def criar_pasta_dados():
    """Cria a pasta de dados caso ela ainda não exista."""
    if not os.path.exists(DADOS_DIR):
        os.makedirs(DADOS_DIR)
        print("Pasta 'dados' criada com sucesso.")


def obter_caminho_arquivo(nome_arquivo):
    """Retorna o caminho absoluto de um arquivo dentro da pasta dados."""
    criar_pasta_dados()
    return os.path.join(DADOS_DIR, nome_arquivo)


def carregar_dados(nome_arquivo):
    """Carrega dados de um arquivo JSON.

    Se o arquivo não existir ou estiver vazio/corrompido, retorna uma lista vazia.
    """
    caminho_arquivo = obter_caminho_arquivo(nome_arquivo)

    try:
        with open(caminho_arquivo, "r", encoding="utf-8") as arquivo:
            return json.load(arquivo)
    except FileNotFoundError:
        print(f"Arquivo {nome_arquivo} não encontrado. Usando lista vazia.")
        return []
    except json.JSONDecodeError:
        print(f"Arquivo {nome_arquivo} inválido. Usando lista vazia.")
        return []


def salvar_dados(dados, nome_arquivo):
    """Salva dados em um arquivo JSON dentro da pasta dados."""
    caminho_arquivo = obter_caminho_arquivo(nome_arquivo)

    try:
        with open(caminho_arquivo, "w", encoding="utf-8") as arquivo:
            json.dump(dados, arquivo, indent=4, ensure_ascii=False)
        print(f"Dados salvos em {nome_arquivo}.")
        return True
    except Exception as erro:
        print(f"Erro ao salvar {nome_arquivo}: {erro}")
        return False


# ============================================================
# FUNÇÕES DE DATA E HORA
# ============================================================

def obter_data_atual():
    """Retorna a data e hora atual no formato usado pelo sistema."""
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def converter_texto_para_data(texto_data):
    """Converte uma data em texto para um objeto datetime."""
    return datetime.strptime(texto_data, "%Y-%m-%d %H:%M:%S")


def calcular_diferenca_horas(data_inicio, data_fim):
    """Calcula a diferença em horas entre duas datas em formato texto."""
    inicio = converter_texto_para_data(data_inicio)
    fim = converter_texto_para_data(data_fim)
    diferenca_em_horas = (fim - inicio).total_seconds() / 3600

    # max evita resultado negativo caso alguma data antiga esteja inconsistente.
    return round(max(diferenca_em_horas, 0), 2)


# ============================================================
# FUNÇÕES DE TEXTO
# ============================================================

def remover_acentos(texto):
    """Remove acentos de um texto."""
    texto_normalizado = unicodedata.normalize("NFD", texto)
    caracteres_sem_acento = []

    for caractere in texto_normalizado:
        if unicodedata.category(caractere) != "Mn":
            caracteres_sem_acento.append(caractere)

    return "".join(caracteres_sem_acento)


def gerar_senha_padrao(nome, identificador):
    """Gera senha no padrão nome+id, sem acentos, espaços e letras maiúsculas."""
    nome_sem_acentos = remover_acentos(nome)
    nome_sem_espacos = nome_sem_acentos.replace(" ", "")
    nome_formatado = nome_sem_espacos.lower()

    return f"{nome_formatado}{identificador}"
