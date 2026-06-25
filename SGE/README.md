# Sistema de Gestão Acadêmica e Financeira com SQLite

## 1. Descrição do Projeto

Este projeto é uma evolução do sistema desenvolvido no Projeto 2. A proposta original trabalhava com o cadastro, consulta, atualização e exclusão de estudantes, além do cálculo automático da média e da situação acadêmica de cada aluno.

No Projeto 4, o sistema foi ampliado para funcionar como uma aplicação mais completa de **gestão acadêmica e financeira**, utilizando banco de dados SQLite para armazenar os registros de estudantes e seus dados financeiros. A base de dados foi populada com **no mínimo 100 registros**, permitindo consultas, listagens, alterações, relatórios e cálculos financeiros com valores monetários em reais.

O sistema é executado pelo terminal, por meio de menus interativos, e permite o gerenciamento de estudantes, mensalidades, descontos, vencimentos, juros e faturamento total.

---

## 2. Problema que o Sistema Resolve

Instituições de ensino precisam organizar dados acadêmicos e financeiros de seus estudantes de forma clara, segura e consultável. O problema resolvido por este sistema é a centralização dessas informações em uma aplicação Python, evitando perda de dados ao encerrar o programa e permitindo que a instituição acompanhe:

- dados cadastrais dos estudantes;
- notas e situação acadêmica;
- mensalidades cadastradas;
- descontos aplicados;
- vencimentos;
- juros por atraso;
- faturamento total.

Dessa forma, o sistema permite uma visão integrada entre a parte acadêmica e a parte financeira da instituição.

---

## 3. Principais Elementos do Sistema

Os principais elementos do sistema são:

| Elemento | Descrição |
|---|---|
| Estudante | Representa o aluno cadastrado no sistema |
| Faculdade | Controla as operações acadêmicas, como cadastro, busca, listagem, atualização e exclusão |
| Financeiro | Controla mensalidades, descontos, vencimentos, juros e relatórios financeiros |
| BancoDeDados | Responsável pela conexão com o SQLite e pelas operações de persistência |
| Banco SQLite | Armazena estudantes e dados financeiros de forma permanente |

---

## 4. Representação dos Dados em Python

O sistema utiliza classes para organizar a lógica principal:

- `Estudante`: armazena matrícula, nome, e-mail, notas, média e status acadêmico.
- `Faculdade`: gerencia os estudantes e se comunica com o banco de dados.
- `Financeiro`: gerencia os valores financeiros vinculados aos estudantes.
- `BancoDeDados`: cria as tabelas e executa comandos SQL para inserir, consultar, atualizar e excluir dados.

Mesmo com o uso do SQLite, o sistema também utiliza listas em Python para carregar os estudantes consultados no banco e exibi-los no terminal.

---

## 5. Estrutura de Dados e Banco de Dados

A versão inicial do Projeto 2 utilizava principalmente listas em memória. No Projeto 4, a estrutura foi evoluída para o uso de um banco de dados SQLite, mantendo a organização em classes Python.

O banco de dados utilizado é o arquivo:

```text
faculdade.db
```

Ele possui duas tabelas principais:

### Tabela `estudantes`

| Campo | Tipo | Descrição |
|---|---|---|
| matricula | INTEGER | Identificador único do estudante |
| nome | TEXT | Nome do estudante |
| email | TEXT | E-mail do estudante |
| nota1 | REAL | Primeira nota |
| nota2 | REAL | Segunda nota |

### Tabela `financeiro`

| Campo | Tipo | Descrição |
|---|---|---|
| id | INTEGER | Identificador do registro financeiro |
| matricula | INTEGER | Matrícula do estudante relacionado |
| mensalidade | REAL | Valor da mensalidade em reais |
| desconto | REAL | Valor do desconto em reais |
| vencimento | TEXT | Data de vencimento da mensalidade |

---

## 6. Relação entre os Elementos

O sistema possui uma relação entre as tabelas `estudantes` e `financeiro`.

A relação implementada é:

```text
Um estudante possui um registro financeiro.
```

Essa relação é feita por meio do campo `matricula`, que aparece nas duas tabelas. Na tabela `financeiro`, a matrícula funciona como chave estrangeira, permitindo associar cada mensalidade a um estudante específico.

### Classificação da Relação

A relação pode ser classificada como **um para um (1:1)**, pois cada estudante pode ter um conjunto principal de informações financeiras cadastrado no sistema.

---

## 7. Funcionalidades do Sistema

O sistema possui um menu principal com as seguintes opções:

```text
1. Cadastrar estudantes
2. Listar estudantes
3. Buscar estudante
4. Atualizar cadastro
5. Excluir cadastro
6. Menu financeiro
0. Sair
```

### Funcionalidades Acadêmicas

- cadastrar novos estudantes;
- listar todos os estudantes cadastrados;
- buscar estudante por matrícula;
- atualizar nome, e-mail e notas;
- excluir cadastro;
- calcular média automaticamente;
- definir status acadêmico como aprovado ou reprovado.

### Funcionalidades Financeiras

- definir mensalidade;
- consultar mensalidade;
- aplicar desconto;
- calcular juros por atraso;
- enviar boleto por e-mail de forma simulada;
- gerar relatório financeiro;
- calcular faturamento original, descontos, juros e faturamento final.

---

## 8. Regras de Validação

O sistema possui regras de validação para evitar entradas incorretas:

- a matrícula deve ser um número inteiro;
- as notas devem estar entre `0.0` e `10.0`;
- o valor da mensalidade não pode ser negativo;
- o desconto não pode ser negativo;
- o desconto não pode ser maior que a mensalidade;
- a data de vencimento deve seguir o formato `dd/mm/aaaa`;
- o sistema verifica se o estudante existe antes de consultar ou alterar dados financeiros.

Essas validações evitam erros durante a execução e melhoram a consistência dos dados cadastrados.

---

## 9. Processamento de Dados

O sistema realiza diferentes tipos de processamento:

### Cálculo da Média

```text
media = (nota1 + nota2) / 2
```

### Critério de Aprovação

```text
Média >= 7.0  → Aprovado
Média < 7.0   → Reprovado
```

### Cálculo Financeiro

O sistema considera mensalidade, desconto e juros para calcular o valor final:

```text
valor_com_desconto = mensalidade - desconto
juros = valor_com_desconto * taxa_juros
valor_final = valor_com_desconto + juros
```

A taxa de juros utilizada no sistema é de `2%`, aplicada quando a data atual é maior que a data de vencimento.

---

## 10. Consultas, Listagens e Resultados Gerados

O sistema permite:

- listar todos os estudantes cadastrados;
- buscar estudante por matrícula;
- consultar mensalidade individual;
- verificar descontos e juros;
- gerar relatório financeiro completo;
- calcular faturamento total da instituição.

O relatório financeiro apresenta informações como:

- matrícula;
- nome;
- e-mail;
- mensalidade;
- desconto;
- juros;
- valor final;
- vencimento;
- faturamento original;
- total de descontos;
- total de juros;
- faturamento final.

---

## 11. Base de Dados Populada

O requisito do Projeto 4 exige uma base com no mínimo **100 registros**. Para atender a esse requisito, foi criado o arquivo:

```text
popular_banco.py
```

Esse arquivo deve ser executado uma única vez para criar e popular o banco de dados com 100 estudantes e seus respectivos dados financeiros.

Comando para popular o banco:

```bash
python popular_banco.py
```

Após a execução, o arquivo `faculdade.db` é criado com os registros iniciais.

Os 100 registros iniciais possuem:

- nome do estudante;
- e-mail;
- matrícula gerada automaticamente;
- nota 1;
- nota 2;
- mensalidade em reais;
- desconto;
- data de vencimento.

Novos estudantes também podem ser cadastrados posteriormente pelo menu principal do sistema. Caso o estudante seja cadastrado sem mensalidade, o valor financeiro poderá ser inserido depois pelo menu financeiro.

---

## 12. Valor Monetário nos Registros

Os registros financeiros possuem valores monetários em reais, atendendo ao requisito de mensuração financeira.

Exemplo de dados financeiros armazenados:

```text
Mensalidade: R$ 850,00
Desconto: R$ 50,00
Juros: R$ 16,00
Valor final: R$ 816,00
```

Esses valores permitem gerar relatórios e análises financeiras da instituição.

---

## 13. Arquitetura do Sistema

```text
PJ4/
│
├── estudantes.py       # Classe Estudante e cálculo de média/status
├── faculdade.py        # Controle acadêmico dos estudantes
├── financeiro.py       # Controle financeiro e relatórios
├── database.py         # Criação e manipulação do banco SQLite
├── popular_banco.py    # Popula o banco com 100 registros iniciais
├── main.py             # Menu principal do sistema
├── faculdade.db        # Banco de dados SQLite populado
└── README.md           # Documentação do projeto
```

---

## 14. Justificativa das Estruturas Utilizadas

### Classes

As classes foram utilizadas para organizar as responsabilidades do sistema:

- `Estudante` concentra os dados e cálculos acadêmicos individuais;
- `Faculdade` concentra as ações acadêmicas;
- `Financeiro` concentra as ações relacionadas a valores monetários;
- `BancoDeDados` concentra a comunicação com o SQLite.

### SQLite

O SQLite foi escolhido por ser simples, leve e fazer parte da biblioteca padrão do Python por meio do módulo `sqlite3`. Ele permite salvar os dados de forma permanente, diferente da lista em memória utilizada inicialmente no Projeto 2.

### Lista em Python

A lista ainda é utilizada para armazenar temporariamente os estudantes retornados do banco durante a execução, facilitando a listagem e a exibição dos dados no terminal.

---

## 15. Instalação e Execução

### Requisitos

- Python 3.6 ou superior;
- biblioteca padrão `sqlite3`;
- todos os arquivos `.py` na mesma pasta.

Não é necessário instalar bibliotecas externas.

### Passo 1 — Popular o banco de dados

Execute apenas uma vez:

```bash
python popular_banco.py
```

Esse comando cria o arquivo `faculdade.db` e insere os 100 registros iniciais.

### Passo 2 — Executar o sistema

```bash
python main.py
```

Depois disso, basta utilizar o menu interativo no terminal.

---

## 16. Demonstração Prática do Funcionamento

Durante a apresentação, o grupo pode demonstrar:

1. execução do sistema pelo `main.py`;
2. listagem dos 100 estudantes cadastrados;
3. busca de estudante por matrícula;
4. cadastro de novo estudante;
5. definição de mensalidade no menu financeiro;
6. aplicação de desconto;
7. consulta de mensalidade;
8. geração do relatório financeiro;
9. exibição do faturamento total.

---

## 17. Evolução em Relação ao Projeto 2

No Projeto 2, o sistema armazenava os estudantes em uma lista durante a execução do programa. Ao encerrar o sistema, os dados eram perdidos.

No Projeto 4, foram implementadas as seguintes melhorias:

- uso de banco de dados SQLite;
- criação de uma base populada com 100 registros;
- persistência dos dados após encerrar o programa;
- inclusão de dados financeiros em reais;
- relação entre estudante e financeiro;
- relatório financeiro com faturamento;
- validações adicionais;
- melhor organização das responsabilidades entre os arquivos.

---

## 18. Atendimento aos Requisitos do Projeto 4

| Item | Requisito | Como foi atendido |
|---|---|---|
| 1 | Definição clara do problema | Controle acadêmico e financeiro de estudantes |
| 2 | Identificação dos principais elementos | Estudante, Faculdade, Financeiro e BancoDeDados |
| 3 | Representação dos dados em Python | Uso de classes e objetos |
| 4 | Uso de lista, tupla, dicionário ou lista de dicionários | Lista de estudantes retornada do banco e tuplas retornadas pelas consultas SQL |
| 5 | Pelo menos uma relação entre elementos | Relação entre estudante e financeiro pela matrícula |
| 6 | Classificação da relação | Relação um para um entre estudante e financeiro |
| 7 | Pelo menos uma regra de validação | Validação de nota, matrícula, valores e data |
| 8 | Pelo menos uma ação que altere ou processe dados | Cadastro, atualização, exclusão, cálculo de média, desconto e juros |
| 9 | Pelo menos uma consulta, listagem ou resultado gerado | Listagem de estudantes, busca por matrícula e relatório financeiro |
| 10 | Comentários explicando a lógica principal | Comentários nos arquivos principais do sistema |
| 11 | Justificativa das estruturas utilizadas | Classes, listas e SQLite explicados na documentação |
| 12 | Demonstração prática do funcionamento | Menu interativo pelo terminal |
| 13 | Banco de dados populado com no mínimo 100 registros | Arquivo `faculdade.db` populado pelo `popular_banco.py` |
| 14 | Valor monetário nos registros principais | Mensalidade, desconto, juros e valor final em reais |
| 15 | Relatório ou cálculo financeiro | Relatório financeiro com faturamento original, descontos, juros e faturamento final |

---

## 19. Conclusão

O sistema desenvolvido atende aos requisitos do Projeto 4 ao apresentar uma aplicação acadêmica e financeira integrada, com banco de dados populado, persistência de informações, relação entre elementos, validações, consultas, processamento de dados e geração de resultados úteis.

A evolução em relação ao Projeto 2 fica evidente pela substituição do armazenamento apenas em memória por banco de dados SQLite, pela inclusão de dados financeiros em reais e pela geração de relatórios para análise.

---

## 20. Autores

Projeto acadêmico desenvolvido para a disciplina de Construção Algorítmica de Soluções e Representação Matemática de Problemas.

Autores:

- Ana Caroline de Proença
- Éter Oliveira Gomes da Silva
- Laura Camilli Stocchero
- Sophia Bogeski Golpian

Desenvolvido como trabalho acadêmico — 2026.
