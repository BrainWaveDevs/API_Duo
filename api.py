#━━━━━━━━━❮Bibliotecas❯━━━━━━━━━
from flask import Flask, jsonify, request, render_template
import unicodedata
#━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━


app = Flask(__name__)

#━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# Lista integrada com alguns alunos
#━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

alunos = ['Joao', 'Maria', 'Pedro', 'Ana']

#━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# Dicionário para armazenar a lista de presença
#━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

presenca = {}

#━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# Função para substituir caracteres especiais por equivalentes sem acentos
#━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

def remover_acentos(texto):
    return unicodedata.normalize('NFKD', texto).encode('ASCII', 'ignore').decode('ASCII')

#━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# Rota para obter a lista de alunos
#━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

@app.route('/alunos', methods=['GET'])
def get_alunos():
    return jsonify(alunos)

#━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# Rota para marcar a presença de um aluno
#━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

@app.route('/presenca', methods=['PUT'])
def update_presenca():
    aluno = request.json['aluno']
    presente = request.json['presente']
    presenca[remover_acentos(aluno)] = presente
    return jsonify(presenca)

#━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# Rota para obter a lista de presença
#━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

@app.route('/presenca', methods=['GET'])
def get_presenca():
    return jsonify(presenca)

if __name__ == '__main__':
    app.run(debug=True)

#━━━━━━━━━━━━━━❮◆❯━━━━━━━━━━━━━━
@app.route('/test', methods=['GET', 'POST'])
def home():
    pred = None
    if request.method == 'POST':
        nome = request.form.get('Nome')
        presenca = request.form.get('Presença')
    return render_template('index.html')
#━━━━━━━━━━━━━━❮◆❯━━━━━━━━━━━━━━
print('')