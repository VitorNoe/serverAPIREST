# Lead Management API

## Introdução ao Projeto

A **Lead Management API** é uma aplicação baseada em Flask para gerenciar leads de vendas. A API permite criar, listar, atualizar e deletar leads, armazenando informações como nome, email, telefone, localização geográfica (latitude e longitude), temperatura e interesse.

## Funcionalidades

- **Listar Leads**: Obter uma lista de todos os leads armazenados no banco de dados.
- **Criar Lead**: Adicionar um novo lead ao banco de dados.
- **Atualizar Lead**: Atualizar as informações de um lead existente.
- **Deletar Lead**: Remover um lead do banco de dados.
- **Buscar Lead Específico**: Obter informações detalhadas de um lead por ID.

## Instruções de Instalação e Execução

### Dependências

Certifique-se de ter o Python 3.8+ instalado. Clone o repositório e instale as dependências necessárias usando o pip:

```bash
git clone https://github.com/seu-usuario/lead-management-api.git
cd lead-management-api
pip install -r requirements.txt
```

##Estrutura do Projeto
lead-management-api/
│
├── app.py                   # Arquivo principal do Flask
├── api_handler.py           # Manipulador de Rotas e Lógica da API
├── lead_service.py          # Lógica de Negócio e Acesso ao Banco de Dados
├── models.py                # Definição do Modelo de Dados com SQLAlchemy
├── database.py              # Conexão e Inicialização do Banco de Dados
├── generate_leads.py        # Script para gerar dados fictícios
├── requirements.txt         # Dependências do projeto
└── README.md                # Documentação do Projeto
