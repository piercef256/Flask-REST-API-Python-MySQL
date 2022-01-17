from flask import Flask
from flask_restful import abort, Api
from flask import request, jsonify

app = Flask(__name__)
api = Api(app)

TODOS = {
    'todo0': {'task': 'build an API'},
    'todo1': {'task': 'accept JSON'},
    'todo2': {'task': 'integrate MySQL'},
    'todo3': {'task': 'profit!'},
}


@app.route('/')
def index():
    return '<h1>Hello World!</h1>'


@app.route('/todos', methods=['GET'])
def get_todos():
    return jsonify({'todos': TODOS})


@app.route('/todos', methods=['POST'])
def create_todo():
    if not request.json or not 'task' in request.json:
        abort(400)
    todo_id = int(max(TODOS.keys()).lstrip('todo')) + 1
    todo_id = 'todo%i' % todo_id
    TODOS[todo_id] = {'task': request.get_json()['task']}
    return jsonify({'todo': TODOS[todo_id]}), 201


@app.route('/todos/<todo_id>', methods=['GET'])
def get_todo(todo_id):
    if todo_id in TODOS:
        return jsonify({'todo': TODOS[todo_id]})
    return jsonify({'message': 'Not found'}), 404


@app.route('/todos/<todo_id>', methods=['DELETE'])
def delete_todo(todo_id):
    if todo_id in TODOS:
        del TODOS[todo_id]
        return jsonify({'message': 'Deleted'}), 200
    return jsonify({'message': 'Not found'}), 404


@app.route('/todos/<todo_id>', methods=['PUT'])
def update_todo(todo_id):
    if todo_id in TODOS:
        TODOS[todo_id] = {'task': request.get_json()['task']}
        return jsonify({'todo': TODOS[todo_id]}), 200
    return jsonify({'message': 'Not found'}), 404


if __name__ == '__main__':
    app.run(debug=True)
