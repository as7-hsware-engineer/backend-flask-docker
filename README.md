# Projeto de Cadastro de Cidades com Flask e PostgreSQL

Este projeto demonstra um aplicativo web simples para cadastrar cidades, construído com o framework Flask (Python) e o banco de dados PostgreSQL.

## Visão Geral

O aplicativo permite aos usuários inserir o nome de uma cidade em um formulário e, em seguida, exibe uma lista de todas as cidades cadastradas em uma tabela.

## Tecnologias Utilizadas

*   **Flask**: Framework web Python para criação de aplicativos web.
*   **PostgreSQL**: Banco de dados relacional para armazenamento persistente das cidades.
*   **Docker**: Plataforma para construir e executar aplicativos em contêineres.
*   **Docker Compose**: Ferramenta para definir e gerenciar aplicativos multi-container Docker.
*   **pgAdmin**: Ferramenta de gerenciamento de banco de dados PostgreSQL (opcional).

## Estrutura de Arquivos
backend/
├── templates/
│   └── index.html
├── app.py
├── database.py
├── Dockerfile-backend
└── requirements.txt
.dockerignore
docker-compose.yml

*   **`backend/templates/index.html`**: Contém o formulário de entrada e a tabela de exibição de cidades.
*   **`backend/app.py`**: Lógica principal do aplicativo Flask, incluindo rotas, conexão com o banco de dados e renderização de templates.
*   **`backend/database.py`**: Script para criar a tabela no banco de dados, se ainda não existir.
*   **`backend/Dockerfile-backend`**: Instruções para construir a imagem Docker do backend.
*   **`backend/requirements.txt`**: Lista as dependências do projeto (Flask e psycopg2-binary).
*   **`.dockerignore`**: Especifica arquivos e diretórios a serem ignorados pelo Docker.
*   **`docker-compose.yml`**: Define os serviços (backend, banco de dados e pgAdmin) e suas configurações.

## Como Executar

1.  **Pré-requisitos:**
    *   Docker e Docker Compose instalados.
2.  **Clonar o repositório:**
    ```bash
    git clone https://[endereço-do-seu-repositório]/cadastro-cidades-flask-postgresql.git
    ```
3.  **Navegar para o diretório do projeto:**
    ```bash
    cd cadastro-cidades-flask-postgresql
    ```
4.  **Iniciar os containers:**
    ```bash
    docker-compose up -d
    ```
5.  **Acessar o aplicativo:**
    Abra o navegador em `http://localhost:5000`.
6.  **Acessar o pgAdmin (opcional):**
    Abra o navegador em `http://localhost:8080`. Use as credenciais padrão (`admin@example.com` e `admin`).

## Funcionalidades

*   **Cadastro de cidades:** O usuário pode inserir o nome de uma cidade no formulário e clicar em "Adicionar" para cadastrá-la no banco de dados.
*   **Listagem de cidades:** A página exibe uma tabela com todas as cidades cadastradas, ordenadas por ID.

## Diagrama de Arquitetura

```mermaid
graph LR
    subgraph Usuário
        A[Navegador] --> B(Servidor Web Flask)
    end
    B --> C{Banco de Dados PostgreSQL}
    B --> D[pgAdmin (opcional)]
    C --> B
Fluxo da Aplicação
O usuário acessa a página web através do navegador.
O navegador envia uma requisição GET para o servidor web Flask.
O servidor web Flask executa a função index() definida em app.py.
A função index() se conecta ao banco de dados PostgreSQL utilizando as credenciais definidas no docker-compose.yml.
A função index() busca todas as cidades cadastradas no banco de dados.
A função index() renderiza o template index.html, incluindo a lista de cidades.
O servidor web Flask envia a resposta HTML para o navegador.
O navegador exibe a página web com o formulário e a tabela de cidades.
O usuário preenche o formulário e clica em "Adicionar".
O navegador envia uma requisição POST para o servidor web Flask.
O servidor web Flask executa a função index() novamente.
A função index() coleta os dados do formulário e insere a nova cidade no banco de dados.
A função index() busca novamente todas as cidades cadastradas no banco de dados.
A função index() renderiza o template index.html atualizado.
O servidor web Flask envia a resposta HTML para o navegador.
O navegador exibe a página web com a nova cidade adicionada à tabela.
