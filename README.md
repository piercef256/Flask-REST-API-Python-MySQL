# Flask-REST-API-Python-MySQL

### What is this project?

- This is a REST API backend built using Flask and MySQL.
- Users can perform C.R.U.D. operations on a todolist MySQL database table.
- REST API endpoint is setup via Microsoft Azure: ```flask-sql.azurewebsites.net/```.

### MySQL setup

1. Create table

```
CREATE TABLE todos (
  id INT NOT NULL AUTO_INCREMENT,
  task VARCHAR(45) NOT NULL,
PRIMARY KEY (`id`));
```

2. Add records

```
INSERT INTO todos(task) VALUES('build an API');
INSERT INTO todos(task) VALUES('accept JSON');
INSERT INTO todos(task) VALUES('integrate MySQL');
INSERT INTO todos(task) VALUES('profit!');
commit;
```

### API Setup

1. Install requirements

```
pip install -r requirements.txt
```

2. Run

```
python api.py
```

### API Use Examples (tests for Postman can be found in tests folder)

#### Create Task
```
Endpoint: http://127.0.0.1:5000/todos
Method: POST
Request Body:
{
    "task":"New task!"
}
```

#### Fetch All Tasks
```
Endpoint: http://127.0.0.1:5000/todos
Method: GET
Request Body:
{
    None
}
```

#### Fetch Single Task (task 1)
```
Endpoint: http://127.0.0.1:5000/todos/{task index}
Endpoint example: http://127.0.0.1:5000/todos/1
Method: GET
Request Body:
{
    None
}
```

#### Update Task (task 1)
```
Endpoint: http://127.0.0.1:5000/todos/{task index}
Endpoint example: http://127.0.0.1:5000/todos/1
Method: PUT
Request Body:
{
    "task":"Updated task"
}
```

#### Delete Task (task 1)
```
Endpoint: http://127.0.0.1:5000/todos/{task index}
Endpoint example: http://127.0.0.1:5000/todos/1
Method: DELETE
Request Body:
{
    None
}
```

