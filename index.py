from flask import Flask, jsonify, request

app = Flask(__name__)

livros = [
    {
        'id': 1,
        'nome': 'Análise de balanços',
        'autor': 'Mary Bufett'
    },
    {
        'id': 2,
        'nome': 'Senhor do anéis',
        'autor': 'J. R. R. Tolkien'
    },
    {
        'id': 3,
        'nome': 'Pai rico, Pai pobre',
        'autor': 'Robert T. Kiyosaki'
    },
]


#consultar todos os livros
@app.route('/livros',methods=['GET'])
def todos_os_livros():
    return jsonify(livros)

#consultar por id
@app.route('/livros/<int:id>',methods=['GET'])
def busca_id(id):
    for livro in livros:
        if livro.get('id') == id:
            return jsonify(livro)

#editar
@app.route('/livros/<int:id>',methods=['PUT'])
def editar(id):
    livro_alterado = request.get_json()
    for index,livro in enumerate(livros):
        if livro.get('id')==id:
            livros[index].update(livro_alterado)
            return jsonify(livros[index])
#criar
@app.route('/livros',methods=['POST'])
def criar_livro():
    novo_livro = request.get_json()
    livros.append(novo_livro)
    return jsonify(livros)

#Excluir
@app.route('/livros/<int:id>',methods = ['DELETE'])
def excluir_livro(id):
    for index, livro in enumerate(livros):
        if livro.get('id') == id:
            del livros[index]
            return jsonify(livros)



app.run(port=5000,host='localhost',debug=True) 