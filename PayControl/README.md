# PayControl - Sistema de Controle de Contas a Pagar

## Sobre o Projeto

O PayControl é um sistema de gerenciamento de contas a pagar desenvolvido em Python com o objetivo de auxiliar pessoas físicas e pequenos negócios no controle financeiro de suas obrigações.

O sistema permite cadastrar, consultar, atualizar, excluir e registrar pagamentos de contas, além de oferecer recursos de controle orçamentário, persistência em banco de dados SQLite, tratamento de datas e geração de relatórios financeiros.

## Problema

O gerenciamento inadequado de contas a pagar pode resultar em atrasos, multas, juros e dificuldades no planejamento financeiro. Muitas pessoas e pequenos negócios enfrentam dificuldades para acompanhar vencimentos, controlar despesas e visualizar o impacto financeiro de seus compromissos.

## Objetivo

Desenvolver uma solução capaz de organizar e controlar contas a pagar, auxiliando usuários na gestão financeira por meio do registro, acompanhamento e análise de despesas, contribuindo para uma tomada de decisão mais eficiente.

## Tecnologias Utilizadas

* Python 3
* SQLite
* Decimal
* Datetime
* Random
* Programação Orientada a Objetos (POO)

## Conceitos Aplicados

O projeto foi desenvolvido utilizando conceitos de:

* Programação Orientada a Objetos (POO)
* Estruturas de Dados
* Banco de Dados SQLite
* Persistência de Dados
* Regras de Negócio
* Controle Financeiro
* Validação de Dados
* Tratamento de Datas

---

# Autores

* Danilo Depetris Soares – BSI
* Enzo Gabriel Miranda da Costa – BSI
* Gabriel Weber da Rocha – BSI
* Julia Barbosa de Almeida – BSI
* Luis Gustavo Bueno Taquete – BSI
* Nityananda Portellada – Engenharia de Software

**Desenvolvido como trabalho acadêmico – 2026**

---

# Objetivo

Desenvolver uma solução capaz de organizar e controlar contas a pagar, auxiliando usuários na gestão financeira por meio do registro, acompanhamento e análise de despesas.

---

# Contextualização

O gerenciamento inadequado de contas a pagar pode resultar em atrasos, multas, juros e dificuldades de planejamento financeiro.

Pensando nisso, o PayControl foi desenvolvido para fornecer uma ferramenta simples e eficiente que permita o acompanhamento das obrigações financeiras, oferecendo informações que auxiliem na tomada de decisões.

---

# Funcionalidades

## Gestão de Contas

* Cadastro de contas
* Atualização de contas
* Exclusão de contas
* Registro de pagamento
* Controle de status

### Classificação Automática de Status

Durante a geração das contas e durante o gerenciamento do sistema, o status das contas pode ser classificado automaticamente conforme a situação da data de vencimento.

Os status utilizados são:

* Pendente;
* Atrasada;
* Paga.

---

## Controle de Orçamento

O sistema permite:

* Definir orçamento total disponível;
* Atualizar orçamento;
* Calcular gastos acumulados;
* Exibir saldo disponível;
* Exibir percentual utilizado;
* Identificar excedentes financeiros.

---

## Consultas

As contas podem ser pesquisadas por:

* ID
* Nome
* Valor
* Dia de vencimento
* Mês de vencimento
* Ano de vencimento

---

## Listagens

O sistema permite listar:

* Todas as contas cadastradas;
* Contas por status;
* Contas por valor;
* Contas por período;
* Contas por período e status;
* Contas ordenadas por impacto financeiro.

---

## Cálculos Financeiros

O sistema calcula:

* Total geral das contas;
* Total por dia;
* Total por mês;
* Total por ano.

---

## Precisão Monetária

Para aumentar a confiabilidade dos cálculos financeiros, o sistema utiliza a biblioteca Decimal do Python.

Essa abordagem reduz problemas de arredondamento comuns em operações monetárias realizadas com números de ponto flutuante.

---

## Relatórios Financeiros

O relatório financeiro apresenta:

* Orçamento total;
* Total gasto;
* Percentual utilizado;
* Saldo restante;
* Excedente financeiro;
* Resumo de gastos por período.

---

# Arquitetura do Sistema

```text
paycontrol/
│
├── main.py
├── cadastro.py
├── conta.py
├── calculo.py
├── movimentacao.py
├── exibir.py
├── contas.db
└── README.md
```

---

## Integração dos Módulos

O sistema foi desenvolvido utilizando uma arquitetura modular.

O arquivo principal (main.py) integra todos os componentes da aplicação e centraliza o fluxo de execução através do menu principal.

Cada módulo possui uma responsabilidade específica:

* Cadastro: gerenciamento das contas e orçamento;
* Movimentação: atualização, exclusão e pagamento;
* Exibir: consultas, listagens e relatórios;
* Cálculo: processamento financeiro;
* Conta: representação das entidades do sistema.

---

# Responsabilidade dos Arquivos

## main.py

Responsável pela execução principal do sistema e pelo menu de navegação.

---

## conta.py

Representa cada conta cadastrada.

### Atributos

* id
* nome_conta
* dia_vencimento
* mes_vencimento
* ano_vencimento
* valor
* status

---

## cadastro.py

Responsável por:

* Cadastro de contas;
* Controle do orçamento;
* Persistência em banco de dados;
* Validação de datas;
* Tratamento de feriados;
* Carregamento de informações.

---

## movimentacao.py

Responsável por:

* Atualização de contas;
* Exclusão de contas;
* Registro de pagamentos.

### Controle de Pagamentos

O sistema permite registrar pagamentos de contas por meio da identificação única (ID).

Durante o processo são realizadas validações para:

* Verificar a existência da conta;
* Impedir pagamentos duplicados;
* Solicitar confirmação da operação;
* Atualizar automaticamente o status da conta para "Paga";
* Persistir a alteração imediatamente no banco de dados.

### Atualização de Informações

As contas cadastradas podem ser atualizadas individualmente através do identificador único (ID).

Os campos disponíveis para atualização incluem:

* Nome da conta;
* Valor;
* Dia de vencimento;
* Mês de vencimento;
* Ano de vencimento;
* Status.

As alterações realizadas são sincronizadas automaticamente com o banco SQLite.

### Exclusão Segura

A exclusão de contas exige confirmação explícita do usuário antes da remoção definitiva do registro.

Após a confirmação:

* O registro é removido do banco de dados;
* O objeto é removido da memória do sistema;
* As alterações são persistidas imediatamente.

---

## calculo.py

Responsável pelos cálculos financeiros do sistema.

---

## exibir.py

Responsável pela apresentação das informações, consultas e relatórios.

---

# Programação Orientada a Objetos

O sistema foi desenvolvido utilizando Programação Orientada a Objetos.

## Classe Conta

Representa uma conta financeira.

Cada objeto armazena:

* Identificação;
* Nome;
* Data de vencimento;
* Valor;
* Status.

---

## Classe Cadastro

Gerencia o conjunto de contas cadastradas e o orçamento do sistema.

---

## Classe Movimentacao

Executa operações de alteração das contas.

---

## Classe Exibir

Responsável pela visualização dos dados.

---

## Classe Calculo

Executa os cálculos financeiros.

---

# Relacionamentos

## Cadastro → Conta

Relacionamento:

```text
1 : N
```

Um cadastro pode conter diversas contas.

Cada conta pertence a apenas um cadastro.

---

## Cadastro → Orçamento

Relacionamento:

```text
1 : 1
```

Existe apenas um orçamento associado ao sistema.

---

# Persistência de Dados

O sistema utiliza SQLite para armazenamento permanente das informações.

## Arquivo do banco

```text
contas.db
```

---

## Tabela de Contas

Armazena:

* ID
* Nome
* Dia
* Mês
* Ano
* Valor
* Status

---

## Tabela de Orçamento

Armazena:

* Valor do orçamento definido pelo usuário.

---

# Estruturas de Dados Utilizadas

## Lista

Utilizada para armazenar as contas em memória.

```python
self.contas = []
```

---

## Lista de Listas

Utilizada para armazenar os feriados.

```python
feriados = [
    ["01-01", "Confraternização Universal"],
    ["12-25", "Natal"]
]
```

---

## Dicionário

Utilizado em relatórios e agrupamentos.

```python
resumo = {}
```

---

## Set

Utilizado para controle de alertas.

```python
self.alertas_disparados = set()
```

---

# Tratamento de Datas

O sistema realiza validações para impedir:

* Datas inexistentes;
* Meses inválidos;
* Dias inválidos;
* Anos fora do intervalo permitido.

---

# Tratamento de Feriados

O sistema possui uma lista de feriados cadastrados.

Quando uma conta é cadastrada em:

* Sábado;
* Domingo;
* Feriado;

O vencimento é automaticamente ajustado para o próximo dia útil disponível.

---

# Controle Orçamentário

O orçamento definido pelo usuário é utilizado como referência para monitoramento dos gastos.

O sistema calcula automaticamente:

* Total gasto;
* Percentual utilizado;
* Saldo disponível;
* Excedente financeiro.

---

# Fluxo Geral do Sistema

```text
Usuário
   ↓
Menu Principal
   ↓
Cadastro de Informações
   ↓
Validação de Dados
   ↓
Persistência em SQLite
   ↓
Consultas
   ↓
Relatórios
   ↓
Controle Financeiro
```

---

# Execução

Abra o terminal na pasta do projeto e execute:

```bash
python main.py
```

---

# Aplicações Práticas

O PayControl pode ser utilizado para:

* Controle financeiro pessoal;
* Planejamento financeiro familiar;
* Controle de despesas domésticas;
* Controle de contas a pagar;
* Pequenos negócios;
* Organização de vencimentos;
* Acompanhamento de orçamento.

---

# Melhorias Futuras

* Interface gráfica;
* Controle de múltiplos usuários;
* Aplicação Web;
* Geração de gráficos;
* Sistema de autenticação.

---

# Informações Acadêmicas

Projeto acadêmico desenvolvido para as disciplinas:

* Construções Algorítmicas de Soluções
* Representação Matemática de Sistemas

Professor Orientador:

**Tiago Pedra**

---

# Licença

Projeto desenvolvido exclusivamente para fins acadêmicos e educacionais.
