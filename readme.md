# Sistema de Folha de Pagamento

## Descrição

O Sistema de Folha de Pagamento foi desenvolvido com o objetivo de simular o gerenciamento de colaboradores de uma empresa e realizar cálculos relacionados à folha salarial.

O projeto permite cadastrar funcionários, armazenar informações em banco de dados e gerar holerites contendo descontos, benefícios e valor líquido do salário.

---

## Funcionalidades

- Cadastro de colaboradores
- Listagem de colaboradores cadastrados
- Armazenamento de dados em banco SQLite
- Controle de benefícios
- Cálculo de INSS
- Cálculo de IRRF
- Cálculo de FGTS
- Cálculo de férias
- Cálculo de salário líquido
- Geração de holerites

---

## Tecnologias Utilizadas

- Python
- SQLite
- Programação Orientada a Objetos (POO)

---

## Estrutura do Projeto

```text
Projeto/
│
├── main.py
├── colaborador.py
├── financas.py
├── folha.db
└── README.md
```

### Arquivos

| Arquivo        | Função                                           |
| -------------- | ------------------------------------------------ |
| main.py        | Controla o funcionamento do sistema              |
| colaborador.py | Classe responsável pelos dados dos colaboradores |
| financas.py    | Realiza todos os cálculos financeiros            |
| folha.db       | Banco de dados SQLite                            |

---

## Banco de Dados

O sistema utiliza SQLite para armazenar as informações dos colaboradores.

Principais dados armazenados:

- Nome
- Cargo
- Salário
- Matrícula
- Dependentes
- Benefícios

---

## Como Executar

1. Instale o Python em sua máquina.
2. Baixe os arquivos do projeto.
3. Abra o terminal na pasta do projeto.
4. Execute o comando:

```bash
python main.py
```

5. Utilize o menu para acessar as funcionalidades do sistema.

---

## Objetivo do Projeto

Este projeto foi desenvolvido para aplicar conceitos de:

- Programação Orientada a Objetos
- Banco de Dados
- Manipulação de dados
- Estruturas de programação em Python

Além disso, o desenvolvimento contou com o apoio de ferramentas de Inteligência Artificial como suporte para estudo, correção de erros e implementação de funcionalidades.

---

## Desenvolvedores

Davi de Almeida Atab
Kauan Machado Vieira 
Sulivan Matheus Leal Tibes
Vinnicius Franco Rodrigues