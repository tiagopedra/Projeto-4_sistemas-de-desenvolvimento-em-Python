---

# Sistema de Help Desk - Atendimento ao Cliente

---

## Nomes dos Integrantes

Arthur Sardinha de Souza  
Abner Elimeleque Sprada  
Alexandre Magno Siqueira Fernandes  
Danilo Maisumi Mota  
Gustavo Salazar Sodré

---

## Área Escolhida

Tecnologia da Informação – Suporte Técnico / Help Desk

---

## Descrição do Projeto

Sistema em Python desenvolvido para gerenciar o fluxo de atendimento técnico de uma empresa de suporte, desde o cadastro do cliente até a resolução do chamado. O sistema permite registrar clientes, gerar chamados automaticamente, classificar problemas, enviar técnico, alterar status, excluir chamados, consultar registros e gerar relatório financeiro com base nos valores cadastrados.

O projeto utiliza Orientação a Objetos, estruturas de dados em Python e banco de dados SQLite para organizar e armazenar as informações dos atendimentos.

---

## Objetivo do Sistema

Automatizar o gerenciamento de chamados técnicos, permitindo o cadastro de clientes, controle de atendimentos, envio de técnicos, atualização do status dos serviços e acompanhamento financeiro dos chamados.

O objetivo é garantir maior organização, rastreabilidade e eficiência no processo de suporte técnico.

---

## Problema que o Sistema Resolve

Empresas que realizam suporte técnico frequentemente enfrentam dificuldades no controle manual de atendimentos, como perda de informações, desorganização de chamados, ausência de histórico, dificuldade no acompanhamento dos serviços e falta de controle financeiro dos atendimentos realizados.

O sistema resolve esse problema ao centralizar as informações dos clientes e chamados em um único ambiente, permitindo melhor controle do atendimento técnico, consulta rápida dos registros, persistência dos dados em banco SQLite e geração de relatório financeiro com valores de manutenção, peças e status de pagamento.

---

## Principais Elementos do Sistema

Os principais elementos do sistema são:

- **Cliente**: pessoa que solicita o atendimento técnico.
- **Chamado**: número gerado automaticamente para identificar cada atendimento.
- **Problema**: descrição ou classificação da falha informada pelo cliente.
- **Empresa**: entidade responsável por gerenciar os clientes, chamados e ações do sistema.
- **Técnico**: representação do envio de atendimento para o chamado.
- **Dados financeiros**: valores de manutenção, peças, quantidade de peças, forma de pagamento e status do pagamento.
- **Banco de dados**: estrutura SQLite utilizada para armazenar os registros cadastrados.

---

## Variáveis do Sistema

Variáveis utilizadas principalmente nas classes `Cliente` e `Empresa`:

| Variável | Tipo | Descrição |
| --- | --- | --- |
| `nome` | String | Nome completo do cliente. |
| `cpf` | String | CPF do cliente, validado com exatamente 11 dígitos numéricos. |
| `contato` | String | Número de telefone do cliente, validado com DDD e 10 ou 11 dígitos. |
| `chamado` | Int | Número do chamado gerado automaticamente pelo sistema. |
| `problema` | String | Descrição do problema técnico informado. |
| `tipo_problema` | String | Classificação entre problema conhecido ou desconhecido. |
| `prazo_resolucao` | String | Prazo estimado de resolução conforme o tipo de problema. |
| `tecnico` | String/None | Indica se o técnico foi enviado para o chamado. |
| `status` | String | Estado atual do chamado, como Indefinido, Técnico enviado, Problema solucionado ou Arquivado. |
| `valor_manutencao` | Float | Valor cobrado pela manutenção. |
| `peca` | String | Peça utilizada no atendimento, se houver. |
| `quantidade_peca` | Int | Quantidade de peças utilizadas. |
| `valor_peca` | Float | Valor unitário da peça utilizada. |
| `forma_pagamento` | String | Forma de pagamento escolhida pelo cliente. |
| `status_pagamento` | String | Situação financeira do chamado: Aguardando orçamento, Pendente, Pago ou Cancelado. |
| `observacao_financeira` | String | Observação adicional sobre o pagamento ou orçamento. |
| `clientes` | Lista | Lista que armazena os objetos de clientes carregados no sistema. |
| `indice` | Dicionário | Dicionário que relaciona o número do chamado ao cliente correspondente. |
| `proximo_chamado` | Int | Controla o próximo número de chamado a ser gerado. |

---

## Estrutura do Projeto

- **`main.py`**: arquivo principal. Exibe o menu interativo e direciona o usuário para as funções do sistema.
- **`cliente.py`**: define a classe `Cliente` e o método `exibir_dados()`.
- **`empresa.py`**: define a classe `Empresa`, inicializa o banco, carrega os clientes salvos e conecta as funções dos demais arquivos.
- **`dados.py`**: contém o cadastro de clientes, alteração de status, validação de CPF, validação de telefone e listas de opções de problemas e status de pagamento.
- **`relatorio.py`**: contém as funções de listagem, pesquisa de chamados e relatório financeiro.
- **`acoes.py`**: contém as ações de envio de técnico e exclusão de chamado.
- **`storage.py`**: contém as funções de conexão, criação, inserção, atualização, exclusão e carregamento de registros no banco SQLite.
- **`helpdesk.db`**: banco de dados SQLite usado para armazenar os chamados cadastrados.

---

## Descrição do Funcionamento

O sistema funciona por meio de um menu interativo no terminal. Ao iniciar o programa pelo arquivo `main.py`, a classe `Empresa` é instanciada, o banco de dados é inicializado e os clientes cadastrados anteriormente são carregados.

O fluxo básico do sistema é:

1. O usuário executa o arquivo `main.py`.
2. O menu principal é exibido no terminal.
3. O usuário escolhe uma das opções disponíveis.
4. No cadastro, o sistema solicita nome, CPF, telefone, problema, valores financeiros e status do pagamento.
5. O CPF é validado com 11 dígitos numéricos.
6. O telefone é validado com DDD e 10 ou 11 dígitos numéricos.
7. O sistema gera automaticamente o número do chamado.
8. O chamado é salvo na lista em memória e no banco de dados SQLite.
9. O usuário pode listar, pesquisar, alterar status, enviar técnico, excluir chamado ou gerar relatório financeiro.

---

## Funcionalidades Implementadas

1. **Cadastrar Cliente**  
   Registra dados pessoais, problema técnico, prazo estimado e informações financeiras.

2. **Listar Clientes**  
   Exibe todos os chamados cadastrados e o total de clientes registrados.

3. **Enviar Técnico**  
   Simula o envio de um técnico, altera o status do chamado para `Técnico enviado` e atualiza o banco de dados.

4. **Pesquisar Chamado**  
   Busca um chamado específico pelo número e exibe todos os dados do cliente.

5. **Alterar Status**  
   Permite atualizar o chamado para `Problema solucionado`, `Chamado Arquivado` ou `Chamado Indefinido`, com persistência no banco.

6. **Excluir Chamado**  
   Remove um chamado da lista, do índice em dicionário e do banco de dados SQLite após confirmação do usuário.

7. **Relatório Financeiro**  
   Gera um resumo financeiro dos chamados cadastrados, calculando totais de manutenção, peças, valor geral, valores pagos, pendentes, aguardando orçamento e cancelados.

8. **Validação de CPF e Telefone**  
   O sistema valida CPF com 11 dígitos e telefone com DDD, aceitando números com 10 ou 11 dígitos.

---

## Relação entre os Elementos do Sistema

O sistema possui uma relação principal entre `Empresa`, `Cliente`, `Chamado` e `Dados Financeiros`.

Classificação das relações:

- **Empresa para Cliente**: relação **1:N**, pois uma empresa pode possuir vários clientes cadastrados.
- **Empresa para Chamado**: relação **1:N**, pois uma empresa pode gerenciar vários chamados.
- **Cliente para Chamado**: relação **1:1**, pois cada cadastro gera um chamado específico para aquele atendimento.
- **Chamado para Problema**: relação **1:1**, pois cada chamado possui um problema principal associado.
- **Chamado para Dados Financeiros**: relação **1:1**, pois cada chamado possui um conjunto de informações financeiras, como valor da manutenção, peça, valor da peça e status do pagamento.

Além disso, o sistema utiliza o dicionário `self.indice`, no qual a chave é o número do chamado e o valor é o cliente correspondente. Essa estrutura cria uma relação direta entre o chamado e o objeto do cliente, facilitando a busca rápida.

---

## Estruturas de Dados Utilizadas

O projeto utiliza diferentes estruturas de dados em Python:

### Classe

A classe `Cliente` foi utilizada para representar cada atendimento de forma organizada. Ela reúne os dados pessoais, técnicos e financeiros do chamado em um único objeto.

A classe `Empresa` foi utilizada para controlar o funcionamento geral do sistema, armazenando clientes, carregando dados do banco e conectando as funcionalidades dos demais arquivos.

### Lista

A lista `self.clientes` armazena todos os clientes carregados no sistema. Ela permite percorrer os registros para listagem, relatórios e contagem de chamados.

### Tupla

As tuplas `PROBLEMAS` e `STATUS_PAGAMENTO` foram utilizadas para armazenar opções fixas do sistema, como tipos de problema, prazos e status de pagamento. Como essas opções não precisam ser alteradas durante a execução, a tupla é uma estrutura adequada.

### Dicionário

O dicionário `self.indice` relaciona o número do chamado ao cliente correspondente. Isso facilita a busca direta de um chamado, evitando percorrer toda a lista em situações normais.

### Banco de Dados SQLite

O SQLite foi utilizado para persistir os dados dos clientes e chamados. Dessa forma, os registros continuam salvos mesmo após o encerramento do programa.

---

## Regras de Validação

O sistema possui regras de validação para evitar cadastros incorretos:

- O nome deve conter apenas letras e espaços.
- O CPF deve conter exatamente 11 dígitos numéricos.
- O CPF não pode ser composto por todos os números iguais.
- O telefone deve conter DDD e possuir 10 ou 11 dígitos numéricos.
- O telefone não pode ser composto por todos os números iguais.
- O DDD deve estar entre 11 e 99.
- As opções de problema devem estar entre 1 e 5.
- As opções de status de pagamento devem estar entre 1 e 4.
- Valores monetários devem ser informados como números.
- Quantidade de peças deve ser informada como número inteiro.

---

## Relatório Financeiro

O relatório financeiro foi implementado no arquivo `relatorio.py`. Ele percorre todos os clientes cadastrados e calcula os valores com base nas informações financeiras de cada chamado.

O cálculo considera:

```python
valor_pecas = valor_peca * quantidade_peca
total_chamado = valor_manutencao + valor_pecas
```

O relatório exibe:

- Total em manutenções.
- Total em peças.
- Valor total dos chamados.
- Total pago.
- Total pendente.
- Total aguardando orçamento.
- Total cancelado.
- Quantidade de chamados pagos.
- Quantidade de chamados pendentes.
- Quantidade de chamados aguardando orçamento.
- Quantidade de chamados cancelados.
- Total de chamados analisados.

Essa funcionalidade atende ao critério de possuir relatório ou cálculo financeiro com base nos valores monetários cadastrados.

---

## Demonstração Prática do Funcionamento

A demonstração prática do sistema será apresentada durante a apresentação do projeto.

Na apresentação, será demonstrado o seguinte fluxo:

1. Execução do arquivo `main.py`.
2. Exibição do menu principal.
3. Cadastro de um cliente.
4. Validação do CPF.
5. Validação do telefone.
6. Geração automática do número do chamado.
7. Pesquisa do chamado cadastrado.
8. Envio de técnico para o chamado.
9. Alteração do status do chamado.
10. Geração do relatório financeiro.
11. Exibição dos dados persistidos no banco SQLite.

Frase utilizada para a apresentação:

> A demonstração prática foi realizada por meio da execução do sistema no terminal, mostrando o cadastro de clientes, validação de CPF e telefone, geração automática de chamados, consulta, alteração de status, envio de técnico, exclusão de registros e geração de relatório financeiro.

---

## Banco de Dados e Registros

O sistema utiliza um banco de dados SQLite chamado `helpdesk.db`.

A tabela principal do banco é `clientes`, contendo os dados pessoais, técnicos e financeiros dos chamados.

O banco de dados do projeto está populado com no mínimo 100 registros, atendendo ao critério de possuir uma estrutura de dados ou banco populado com registros suficientes para testes, consultas e relatórios.

---

## Menu do Sistema

O menu principal apresenta as seguintes opções:

```text
SISTEMA DE HELP DESK
1. Cadastrar cliente
2. Total de clientes
3. Enviar técnico
4. Pesquisar chamado
5. Alterar status do chamado
6. Excluir chamado
7. Relatório financeiro
0. Sair
```

---

## Tecnologias Utilizadas

- **Linguagem**: Python 3.x
- **Paradigma**: Orientação a Objetos
- **Banco de Dados**: SQLite
- **Biblioteca utilizada**: `sqlite3`
- **Estruturas de dados**: listas, tuplas e dicionários

---

## Instruções de Execução

1. Certifique-se de ter o Python instalado.
2. Mantenha os arquivos do projeto na mesma pasta.
3. Execute o comando no terminal:

```bash
python main.py
```

4. Escolha uma das opções do menu para utilizar o sistema.

---

## Justificativa das Estruturas Utilizadas

A estrutura do sistema foi organizada em vários arquivos para facilitar a leitura, manutenção e separação de responsabilidades.

- A classe `Cliente` foi criada para representar cada chamado como um objeto com atributos próprios.
- A classe `Empresa` foi criada para centralizar o controle geral do sistema.
- A lista `self.clientes` foi utilizada para armazenar e percorrer os clientes durante a execução.
- O dicionário `self.indice` foi utilizado para permitir busca rápida pelo número do chamado.
- As tuplas `PROBLEMAS` e `STATUS_PAGAMENTO` foram utilizadas porque representam opções fixas do sistema.
- O banco SQLite foi escolhido para garantir que os dados continuem salvos após o encerramento do programa.
- A separação em arquivos como `dados.py`, `relatorio.py`, `acoes.py` e `storage.py` facilita a organização do código e torna o projeto mais profissional.

---

## Possíveis Melhorias Futuras

- Criar uma interface gráfica para facilitar o uso do sistema.
- Implementar sistema de login para usuários, técnicos e administradores.
- Criar níveis de prioridade para os chamados.
- Gerar relatórios exportáveis em PDF ou Excel.
- Integrar o sistema com WhatsApp ou e-mail para envio de notificações.
- Criar um painel visual com indicadores de chamados abertos, resolvidos, pagos e pendentes.
- Implementar validação completa do CPF pelos dígitos verificadores.

---
