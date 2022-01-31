import pymysql
from db_config import mysql
from flask import jsonify
from flask import request
from app import app


@app.errorhandler(404)
def not_found(error=None):
    message = {
        "status": 404,
        "message": "Not Found: " + request.url,
    }
    resp = jsonify(message)
    resp.status_code = 404

    return resp


def create_todo():
    try:
        _json = request.json
        _task = _json['task']
        _id = None
        
        # check if id exist in _json
        if 'id' in _json:
            _id = _json['id']

              

        # validate the received values
        if _task and request.method == "POST":
            # save edits
            sql = "INSERT INTO todos(task) VALUES(%s)"
            data = (_task)
            if _id is not None:
                data = (_id, _task)
                sql = "INSERT INTO todos VALUES(%s, %s)"
                
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.execute(sql, data)
            conn.commit()
            resp = jsonify("Todo added successfully!")
            resp.status_code = 201
            return resp
        else:
            return not_found()
    except Exception as e:
        print(e)
    finally:
        cursor.close()
        conn.close()


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
