# Backend Rick and Morty

Este projeto implementa uma API utilizando Flask e Python para fornecer dados dos personagens da série Rick and Morty. A API permite consulta de todos os personagens disponíveis, pesquisa paginada e também a pesquisas por ID.

## Tecnologias Usadas
- Python (versão 3.x)
- Flask

## Instalação

### Pré-requisitos
- Python
- Postgresql

### Passos de instalação
1. Clone o repositório:
   ```bash
   git clone https://github.com/thiagossmarins/backend-rick-and-morty.git

2. Entre no diretório do projeto:
   ```bash
   cd backend-rick-and-morty

3. Crie e ative um ambiente virtual:
   ```bash
   python3 -m venv venv
   .\venv\Scripts\activate

4. Instale as dependências:
   ```bash
   pip freeze > requirements.txt

5. Rode o servidor Flask:
   ```bash
   flask run --debug

6. Criar arquivo .env:
    ```bash
   Crie um arquivo como o .env.example

5. Configurar o caminho do seu banco de dados no .env:
   ```bash
   DATABASE_URI = "localhost_url"

### Exemplos de Uso

1. Para buscar todos os personagens:
   ```bash
   Acesse a API no navegador em http://127.0.0.1:5000/characters

2. Para buscar um personagem por ID:
   ```bash
   Acesse a API no navegador em http://127.0.0.1:5000/1

3. Para realizar uma pesquisa paginada (exemplo de pesquisa por nome):
   ```bash
   Acesse a API no navegador em http://127.0.0.1:5000/?page=1&term=Rick
