from flask import Flask, request, jsonify
from tinydb import TinyDB, Query

app = Flask(__name__)

db = TinyDB('banco_de_dados.json')

faltas_table = db.table('faltas')

@app.route('/faltas', methods=['POST'])
def cadastrar_falta():
    data = request.get_json()
    aluno_id = data['aluno_id']
    curso_id = data['curso_id']
    
    aluno = alunos_table.get(doc_id=aluno_id)
    if not aluno:
        return jsonify({'error': 'Aluno não encontrado'}), 404
    
    curso = cursos_table.get(doc_id=curso_id)
    if not curso:
        return jsonify({'error': 'Curso não encontrado'}), 404
    
    faltas_table.insert({'aluno_id': aluno_id, 'curso_id': curso_id})
    
    return jsonify({'message': 'Falta cadastrada com sucesso'}), 201
if __name__ == '__main__':
     app.run(debug=True)