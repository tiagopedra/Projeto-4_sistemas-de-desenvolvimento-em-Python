## Sistema de Gerenciamento de Manutenção DE ATIVOS DE TI: REPAIRA

---

### 📋 Descrição do Projeto
 
Sistema desktop desenvolvido em Python puro para gerenciamento de manutenção de ativos de tecnologia da informação (computadores) e funcionários. O sistema permite o cadastro de equipamentos, abertura e acompanhamento de ordens de serviço, controle de status dos computadores, monitoramento de prazos de atendimento (SLA) e consulta ao histórico completo de manutenções realizadas.

Além disso, o sistema também conta com um módulo de gerenciamento de funcionários, permitindo o cadastro de colaboradores e cálculo do valor da hora com base na carga horária, além do controle dessas informações por parte do gerente.

O projeto foi desenvolvido como trabalho acadêmico, com o objetivo de aplicar e demonstrar conceitos fundamentais de programação em Python, organização modular, persistência de dados em arquivos JSON e aplicação de regras de negócio.

---

### Variáveis Relevantes

Variáveis de computador

| Variável | Tipo | Descrição |
|---------|------|------------|
| id | Inteiro | Identificador único do computador |
| nome | String | Nome do equipamento |
| tipo | String | Tipo do computador (Desktop, Notebook ou All-in-One) |
| modelo | String | Modelo do equipamento |
| processador | String | Processador instalado |
| memoria_ram | String | Quantidade de memória RAM |
| armazenamento | String | Capacidade de armazenamento |
| sistema_operacional | String | Sistema operacional instalado |
| localizacao | String | Local físico do equipamento |
| departamento | String | Departamento responsável |
| status | String | Situação atual do computador |
| data_cadastro | String | Data e hora de cadastro |
| ultima_manutencao | String | Data da última manutenção |

Variáveis do Funcionário

| Variável | Tipo | Descrição |
| id_funcionario| Inteiro | Identificador único do funcionário |
| nome | String | Nome do funcionário |
| cargo | String | Cargo (Estagiário, Júnior, Pleno, Sênior, Gerente) |
| salario_liquido | Float | Salário mensal do funcionário |
| carga_horaria | String | Tipo de carga horária (ex: 40h semanais) |
| horas_mensais | Inteiro | Quantidade de horas mensais trabalhadas |
| salario_por_hora | Float | Valor da hora trabalhada |
| senha | String | Senha gerada automaticamente |
| ativo | Boolean | Indica se o funcionário está ativo |
| data_cadastro | String | Data de cadastro |

---

### Contexto e Problema
 
**Contexto**: Empresas e instituições possuem diversos computadores distribuídos entre setores e departamentos, que necessitam de manutenção preventiva e corretiva para garantir a continuidade das atividades, com a necessidade de uma aba para a gestão e apoio a organização da equipe.


**Problema a Resolver**: A ausência de um sistema centralizado que integre o controle de ativos de TI com a gestão de funcionários dificulta a organização das manutenções e da equipe responsável. Isso pode gerar falhas na distribuição de tarefas, falta de controle sobre a carga horária e remuneração dos colaboradores, além de impactar negativamente na produtividade e no cumprimento dos prazos de atendimento.


**Aplicação Prática**:
- Controle de inventário de ativos de TI
- Registro e acompanhamento de manutenções
- Monitoramento de prazos de atendimento (SLA)
- Histórico para análise de problemas recorrentes
- Gestão de funcionários e serviço de manutenção 
- Controle de carga horária e cálculo de remuneração dos colaboradores
- Apoio à organização de equipes e distribuição de tarefas

---

### 🏗️ Arquitetura do Sistema


REPAIRA/
│
├── src/
│   ├── main.py                     # Menu principal do sistema
│   ├── utils.py                    # Funções utilitárias
│   ├── historico.py                # Histórico e estatísticas
│   ├── funcionarios.py             # Gestão de funcionários
│   ├── monetario.py                # Cálculos financeiros (salários)
│
│   ├── dados/                      # Persistência em arquivos JSON
│   │   ├── computadores.json
│   │   ├── funcionarios.json
│   │   └── ordem_servico.json
│
│   ├── computadores/              # Módulo de computadores
│   │   ├── __init__.py
│   │   ├── computadores.py
│   │   ├── computadores_cadastro.py
│   │   ├── computadores_consulta.py
│   │   ├── computadores_status.py
│   │   └── computadores_repo.py
│
│   ├── ordens/                    # Módulo de ordens de serviço
│   │   ├── __init__.py
│   │   ├── ordens.py
│   │   ├── ordens_cadastro.py
│   │   ├── ordens_consulta.py
│   │   ├── ordens_status.py
│   │   ├── ordens_sla.py
│   │   └── ordens_repo.py
│
└── README.md

```

---

### 🚀 Instalação e Configuração

#### Requisitos
- Python 3.8 ou superior
- Windows, Linux ou macOS

#### Instalação
1- Baixe ou clone o projeto:
```
git clone https://github.com/Aszinnnn/REPAIRA/
```
2- Acesse a pasta do projeto:
```
cd REPAIRA/src
```

3- Execute o sistema:
```
python main.py
```

O sistema utiliza apenas bibliotecas padrão do Python, não sendo necessária a instalação de dependências adicionais.

---

### 📖 Como Usar

Execute o sistema via terminal:
```bash
python main.py
```

O sistema apresenta um menu interativo com as seguintes seções:

#### 1️⃣ Gerenciar Computadores
- Cadastrar computador
- Listar computadores
- Atualizar status
- Deletar computador

#### 2️⃣ Gerenciar Ordens de Serviço
- Abrir nova ordem de serviço
- Atualizar status da ordem
- Verificar prazos de SLA

#### 3️⃣ Histórico e Estatísticas
- Histórico completo de manutenções
- Histórico por computador
- Estatísticas gerais
- Alertas de SLA

#### 4️⃣ Gerenciar Funcionários
- Cadastrar funcionário
- Listar funcionários

 ---

### 🧮 Modelagem do Problema

#### Definição Formal

**Estrutura do Computador**
```python
{
  "id": int,
  "nome": str,
  "tipo": str,
  "modelo": str,
  "processador": str,
  "memoria_ram": str,
  "armazenamento": str,
  "sistema_operacional": str,
  "localizacao": str,
  "departamento": str, 
  "status": str,
  "data_cadastro": str,
  "ultima_manutencao": str
}
```

**Estrutura da Ordem de Serviço**
```python
{
  "id_os": int,
  "id_computador": int,
  "nome_computador": str,
  "tipo_manutencao": str,
  "descricao": str,
  "prioridade": str,
  "tecnico_responsavel": str,
  "data_abertura": str,
  "data_conclusao": str,
  "status": str,
  "sla_previsto": str,
  "solucao_aplicada": str
}
```

**Estrutura do Funcionário**
```python
{
  "id_funcionario": int,
  "senha": str,
  "nome": str,
  "cargo": str,
  "salario_liquido": float,
  "carga_horaria": str,
  "horas_mensais": int,
  "salario_por_hora": float,
  "ativo": bool,
  "data_cadastro": str
}
```

---

### 📈 Métricas de Execução

O sistema registra automaticamente:
- Total de computadores cadastrados
- Total de ordens de serviço
- Ordens abertas e concluídas
- Distribuição por tipo de manutenção
- Distribuição por prioridade
- Alertas de SLA
- Total de funcionários cadastrados
- Cálculo de salário com base na carga horária 

---

### 🧪 Testes

Os testes são realizados manualmente por meio das funcionalidades do sistema:
- Cadastro com validação de dados
- Abertura de OS apenas para computadores existentes
- Atualização correta de status
- Persistência em arquivos JSON
- Carregamento automático de dados na inicialização
- Cadastro de funcionários
- Cálculo automático do salário por hora com base na carga 

---

### 📊 Análise de Sensibilidade

- Testes com diferentes prioridades de ordens
- Verificação do impacto no SLA
- Testes completos do fluxo de status das ordens
- Análise de consistência do histórico
- Testes de ativação/desativação de funcionários
- Impacto de diferentes cargas horárias no cálculo salarial


---

### 🔍 Validação e Comparação

| Funcionalidade | Processo Manual | Sistema Proposto |
|--------------|----------------|------------------|
| Controle de equipamentos | ❌ | ✅ |
| Controle de SLA | ❌ | ✅ |
| Histórico de manutenções | ❌ | ✅ |
| Estatísticas | ❌ | ✅ |
| Controle de funcionários | ❌ | ✅ |
| Cálculo de salário por hora trabalhada | ❌ | ✅ |

---

### 📝 Decisões de Pré-processamento

- Validação dos dados de entrada
- Padronização de textos e datas
- Geração automática de identificadores
- Persistência separada por tipo de dado
- Salvamento automático após cada operação

---

### 🎯 Resultados Esperados

- Organização e controle de ativos de TI
- Redução de falhas e retrabalho
- Cumprimento de prazos de manutenção
- Histórico confiável para auditoria
- Suporte à tomada de decisões
- Melhor gestão de recursos humanos integrados ao sistema
- Melhor organização da equipe

---

### 🤝 Contribuições
 
Projeto acadêmico desenvolvido para a disciplina de **Programação em Python**.

---

### 📄 Licença
 
Uso educacional – código aberto para fins de aprendizado.

---

### 👥 Autores
 
Achilles de Souza Correia  
Isabelle Galvão Ribas  
Juliana Dietz Janisset  
Thiago Augusto Pini Ceccoti  

Desenvolvido como trabalho acadêmico – 2026

