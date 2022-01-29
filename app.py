from flask import Flask
from flask_cors import CORS, cross_origin
app = Flask(__name__)
cors = CORS(app)
import api


@app.route("/")
def hello():
    return "Hello, Todo List!"


@app.route("/todos", methods=["POST"])
def create_todo():
    return api.create_todo()


@app.route("/todos", methods=["GET"])
def fetch_todos():
    return api.todos()


@app.route("/todos/<id>", methods=["GET"])
def fetch_todo(id):
    return api.todo(id)


@app.route("/todos/<id>", methods=["PUT"])
def update_todo(id):
    return api.update_todo(id)



@app.route("/todos/<id>", methods=["DELETE"])
def delete_todo(id):
        return api.delete_todo(id)


if __name__ == "__main__":
    app.run()