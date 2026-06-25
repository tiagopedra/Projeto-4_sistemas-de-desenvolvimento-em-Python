# ## Sistema OrderFlow: Vendas e Pedidos

O **OrderFlow** é um sistema modular desenvolvido em Python projetado para gerenciar com eficiência o fluxo de vendas, o cadastro de produtos e o controle de pedidos. O projeto foi estruturado seguindo boas práticas de modularização para garantir fácil manutenção, escalabilidade e separação clara de responsabilidades.

---

## 👥 Criadores / Desenvolvedores

Este projeto foi idealizado e desenvolvido por:
* **Morôni de Oliveira Gonçalves**
* **Leonardo Oliveira Lima**
* **Gabriel Aquino**
* **Pedro Henrique Natal**

---

## 📁 Estrutura do Projeto e Arquitetura

A arquitetura do sistema é dividida em módulos específicos, organizados da seguinte forma:

* 📂 **`SISTEMA ORDERFLOW VENDAS E PEDIDOS/`** (Diretório Principal)
  * 📄 **`main.py`**: O ponto de entrada (entry point) da aplicação. Inicializa a interface/fluxo principal e orquestra a execução do sistema.
  * 📄 **`sistema.py`**: Core do negócio. Contém a lógica central, regras de validação e integra os demais módulos (produtos, pedidos e banco de dados).
  * 📄 **`pedido.py`**: Gerencia o ciclo de vida dos pedidos (criação, alteração de status, cálculo de totais e associação com clientes).
  * 📄 **`produto.py`**: Define o modelo de dados e propriedades fundamentais dos produtos (ID, nome, preço, descrição e controle de estoque).
  * 📄 **`catalogo.py`**: Responsável pelo agrupamento, indexação, filtros e exibição dos produtos cadastrados e disponíveis para venda.
  * 📄 **`bancodados.py`**: Camada de persistência do sistema. Cuida do salvamento, leitura e integridade dos dados estruturados de produtos e pedidos.

---

## 💻 Requisitos Mínimos do Sistema

Para garantir a execução correta e sem falhas do sistema OrderFlow, certifique-se de cumprir os seguintes requisitos:

### ⚙️ Requisitos de Hardware
* **Processador:** Qualquer processador Dual-Core moderno (Intel Core i3, AMD Ryzen 3 ou equivalente/superior).
* **Memória RAM:** Mínimo de 2 GB de RAM disponíveis.
* **Armazenamento:** Menos de 50 MB de espaço livre em disco (sistema leve focado em console/terminal).

### 🛠️ Requisitos de Software e Ambiente
* **Sistema Operacional:** Windows 10/11, macOS (10.15 ou superior) ou Distribuições Linux (Ubuntu, Debian, Fedora, etc.).
* **Interpretador Python:** **Python 3.8** ou superior instalado de forma global ou em ambiente virtual (`venv`).
* **Dependências de Bibliotecas:** O projeto foi construído utilizando majoritariamente a biblioteca padrão do Python (*Standard Library*). Caso alguma biblioteca externa seja implementada posteriormente, certifique-se de ter o gerenciador de pacotes `pip` atualizado.

---

## 🚀 Como Executar o Projeto (Passo a Passo)

Siga as instruções abaixo para clonar, configurar e rodar o sistema em sua máquina local:

### 1. Clonar ou Baixar o Repositório
Se você utiliza o Git, clone o repositório utilizando o terminal:
```bash
git clone [https://github.com/seu-usuario/nome-do-repositorio.git](https://github.com/seu-usuario/nome-do-repositorio.git)