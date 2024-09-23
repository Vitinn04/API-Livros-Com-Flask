from flask import Flask, jsonify, request

app = Flask(__name__)

livros = [
    {
        'id': 1,
        'titulo': 'Percy Jackson e o ladrão de raios',
        'autor': 'Rick Riordan'
    },
    {
        'id': 2,
        'titulo': 'Harry Potter e a Pedra Filosofal',
        'autor': 'J.K. Rowling'
    },
    {
        'id': 3,
        'titulo': 'O Senhor dos Anéis: A Sociedade do Anel',
        'autor': 'J.R.R. Tolkien'
    }
]

# Consultar(todos)
@app.route('/livros', methods=['GET'])
def obterLivros():
    return jsonify(livros)

# Consultar(id)
@app.route('/livros/<int:id>', methods=['GET'])
def obterLivroId(id):
    for livro in livros:
        if livro.get('id') == id:
            return jsonify(livro)

    return jsonify({'Erro': 'Livro não encontrado'}), 404

#Criar
@app.route('/livros', methods=["POST"])
def criarLivro():
    novoLivro = request.get_json()
    livros.append(novoLivro)

    return jsonify(livros)

# Editar
@app.route('/livros/<int:id>', methods=['PUT'])
def editarLivroId(id):
    livroAlterado = request.get_json()
    for i, livro in enumerate(livros):
        if livro.get('id') == id:
            livros[i].update(livroAlterado)
            return jsonify(livros[i])

    return jsonify({'Erro': 'Livro não encontrado'}), 404

# Excluir
@app.route('/livros/<int:id>', methods=['DELETE'])
def deletarLivroId(id):
    for i, livro in enumerate(livros):
        if livro.get('id') == id:
            del livros[i]
        else:
            return jsonify({'Erro': 'Livro não encontrado'}), 404

    return jsonify(livros)

app.run(port=5000, host='localhost', debug=True)
