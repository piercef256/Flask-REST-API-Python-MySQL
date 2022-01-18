import pymysql
from app import app
from db_config import mysql
from flask import jsonify
from flask import request


@app.errorhandler(404)
def not_found(error=None):
    message = {
        "status": 404,
        "message": "Not Found: " + request.url,
    }
    resp = jsonify(message)
    resp.status_code(404)

    return resp


@app.route("/todos", methods=["GET"])
def todos():
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute("SELECT * FROM todos")
        rows = cursor.fetchall()
        resp = jsonify(rows)
        resp.status_code = 200
        return resp
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


@app.route("/todos", methods=["POST"])
def create_todo():
    try:
        _json = request.json
        _task = _json['task']

        # validate the received values
        if _task and request.method == "POST":
            # save edits
            sql = "INSERT INTO todos(task) VALUES(%s)"
            data = (_task)
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.execute(sql, data)
            conn.commit()
            resp = jsonify("Todo added successfully!")
            resp.status_code = 200
            return resp
        else:
            return not_found()
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


@app.route("/todos/<id>", methods=["GET"])
def todo(id):
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute("SELECT * FROM todos WHERE id=%s", id)
        row = cursor.fetchone()
        resp = jsonify(row)
        resp.status_code = 200
        return resp
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


@app.route("/todos/<id>", methods=["PUT"])
def update_todo(id):
    try:
        _json = request.json
        _task = _json['task']

        # validate the received values
        if _task and request.method == "PUT":
            # save edits
            sql = "UPDATE todos SET task=%s WHERE id=%s"
            data = (_task, id,)
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.execute(sql, data)
            conn.commit()
            resp = jsonify("Todo updated successfully!")
            resp.status_code = 200
            return resp
        else:
            return not_found()
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


@app.route("/todos/<id>", methods=["DELETE"])
def delete_todo(id):
    try:
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM todos WHERE id=%s", (id,))
        conn.commit()
        resp = jsonify("Todo deleted successfully!")
        resp.status_code = 200
        return resp
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


if __name__ == "__main__":
    app.run()
