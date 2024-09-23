# API de Livros com Flask

Esta API permite a criação, consulta, edição e exclusão de livros usando Flask. A API possui os seguintes endpoints:
- **GET** `/livros`: Retorna todos os livros cadastrados.
- **GET** `/livros/<id>`: Retorna um livro específico pelo ID.
- **POST** `/livros`: Adiciona um novo livro à lista.
- **PUT** `/livros/<id>`: Edita um livro específico pelo ID.
- **DELETE** `/livros/<id>`: Remove um livro específico pelo ID.

## Requisitos

- [Python 3.x](https://www.python.org/downloads/)
- [Flask](https://flask.palletsprojects.com/en/2.0.x/installation/)

## Instalação

1. Clone este repositório:

   ```bash
   git clone https://github.com/seu-usuario/seu-repositorio.git
   cd seu-repositorio
   
2. Instale as dependências:

   ```bash
   pip install Flask

# Executando a API

1. No diretório raiz, execute o seguinte comando para iniciar o servidor Flask:

   ```bash
   python app.py

2. A API estará disponível em http://localhost:5000.

