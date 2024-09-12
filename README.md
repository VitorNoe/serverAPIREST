# serverAPI

## Introdução

Este projeto é uma API RESTful desenvolvida para gerenciar leads. A API permite criar, listar, atualizar e deletar leads, fornecendo uma interface eficiente para manipulação de dados de leads para sistemas de CRM (Customer Relationship Management) ou qualquer outro sistema que precise gerenciar informações de contatos e possíveis clientes.

### Funcionalidades

- **Criação de Leads**: Permite a inserção de novos leads no sistema.
- **Listagem de Leads**: Permite a consulta de todos os leads cadastrados.
- **Atualização de Leads**: Permite a atualização dos dados de um lead específico.
- **Deleção de Leads**: Permite a remoção de um lead específico do sistema.

## Instruções de Instalação e Execução

### Pré-requisitos

- [Node.js](https://nodejs.org/) (versão 14.x ou superior)
- [npm](https://www.npmjs.com/) (Node Package Manager)
- [Git](https://git-scm.com/)

### Passo a Passo de Instalação

1. Clone o repositório para sua máquina local:

    ```bash
    git clone https://github.com/seu-usuario/seu-repositorio.git
    cd seu-repositorio
    ```

2. Instale as dependências necessárias:

    ```bash
    npm install
    ```

3. Configure o arquivo `.env` com as variáveis de ambiente necessárias (exemplo abaixo):

    ```env
    PORT=3000
    DB_HOST=localhost
    DB_USER=root
    DB_PASS=password
    DB_NAME=leads_db
    ```

4. Execute a API:

    ```bash
    npm start
    ```

5. A API estará disponível em `http://localhost:3000`.

## Exemplos de Uso da API

### 1. Criar um Lead

**Endpoint**: `POST /leads`

**Exemplo de Requisição:**

```bash
curl -X POST http://localhost:3000/leads -H "Content-Type: application/json" -d '{"nome": "João da Silva", "email": "joao@email.com", "telefone": "123456789"}'
