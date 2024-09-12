# Lead Management API

## Introdução ao Projeto

Este projeto é uma aplicação baseada em Flask para gerenciar leads de vendas. A API permite criar, listar, atualizar e deletar leads, armazenando informações como nome, email, telefone, localização geográfica (latitude e longitude), temperatura e interesse.

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

### Configuração do Banco de Dados

A aplicação utiliza o SQLite como banco de dados padrão. Para inicializar o banco de dados, execute o seguinte comando:

```bash
python -c "from app import db; db.create_all()"
```

### Executando a Aplicação

Para iniciar o servidor Flask, execute:

```bash
python app.py
```

A aplicação estará disponível em `http://127.0.0.1:5000`.

## Exemplos de Uso da API

Aqui estão alguns exemplos de como utilizar a API utilizando o `curl`:

### Listar Todos os Leads

```bash
curl -X GET http://127.0.0.1:5000/leads
```

### Criar um Novo Lead

```bash
curl -X POST http://127.0.0.1:5000/leads -H "Content-Type: application/json" -d '{
    "name": "John Doe",
    "email": "john.doe@example.com",
    "telefone": "(11) 99999-8888",
    "latitude": -23.55052,
    "longitude": -46.633308,
    "temperature": 25.6,
    "interest": "Tecnologia"
}'
```

### Atualizar um Lead

```bash
curl -X PUT http://127.0.0.1:5000/leads/1 -H "Content-Type: application/json" -d '{
    "name": "John Doe Updated",
    "email": "john.doe@example.com",
    "telefone": "(11) 99999-8888",
    "latitude": -23.55052,
    "longitude": -46.633308,
    "temperature": 27.0,
    "interest": "Saúde"
}'
```

### Deletar um Lead

```bash
curl -X DELETE http://127.0.0.1:5000/leads/1
```

### Buscar um Lead por ID

```bash
curl -X GET http://127.0.0.1:5000/leads/1
```

## Detalhes sobre Cada Rota da API

| Rota              | Método | Descrição                                      | Parâmetros                              | Retorno                            |
|-------------------|--------|------------------------------------------------|------------------------------------------|-------------------------------------|
| `/leads`          | GET    | Retorna uma lista de todos os leads.            | Nenhum                                   | Lista de leads em formato JSON.    |
| `/leads/<id>`     | GET    | Retorna um lead específico pelo ID.             | `id`: ID do lead                         | Dados do lead em formato JSON.     |
| `/leads`          | POST   | Cria um novo lead.                              | `name`, `email`, `telefone`, `latitude`, `longitude`, `temperature`, `interest` | Mensagem de sucesso e código 201.  |
| `/leads/<id>`     | PUT    | Atualiza um lead existente pelo ID.             | `id`: ID do lead + campos a serem atualizados | Mensagem de sucesso.               |
| `/leads/<id>`     | DELETE | Deleta um lead específico pelo ID.              | `id`: ID do lead                         | Mensagem de sucesso.               |

## Estrutura do Projeto

```plaintext
lead-management-api/
│
├── app.py                   # Arquivo principal do Flask
├── api_handler.py           # Manipulador de Rotas e Lógica da API
├── lead_service.py          # Lógica de Negócio e Acesso ao Banco de Dados
├── models.py                # Definição do Modelo de Dados com SQLAlchemy
├── database.py              # Conexão e Inicialização do Banco de Dados
├── requirements.txt         # Dependências do projeto
└── README.md                # Documentação do Projeto
```
