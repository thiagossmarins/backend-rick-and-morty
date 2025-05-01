# Backend Rick and Morty

Este projeto implementa uma API utilizando Flask e Python para fornecer dados dos personagens da série Rick and Morty. A API permite consulta de todos os personagens disponíveis , pesquisa paginada e também a pesquisas por ID.

## Tecnologias Usadas
- Python (versão 3.x)
- Flask
- Requests (para consumir a API oficial do Rick and Morty)

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
   .\venv\Scripts\activateyes

4. Instale as dependências:
   ```bash
   pip freeze > requirements.txt

5. Rode o servidor Flask:
   ```bash
   flask run --debug

Acesse a API no navegador em http://127.0.0.1:5000/characters.
