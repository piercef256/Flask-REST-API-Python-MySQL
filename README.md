# Flask-REST-API-Python-MySQL

### What is this project?

- This is a REST API backend webapp built using Flask and MySQL.
- The MySQL database is deployed using AWS RDS, the Flask server is deployed using Azure.
- Users can perform C.R.U.D. operations on the todolist MySQL database by making POST, GET, PUT, and DELETE HTTP requests.
- Users also have the option to setup their own MySQL server information by creating a .env file (more below).

### API Use Examples (tests for Postman can be found in tests folder)

#### Create Task
```
Endpoint: http://flask-sql.azurewebsites.net/todos
Method: POST
Request Body:
{
    "task":"New task!"
}
```

#### Fetch All Tasks
```
Endpoint: http://flask-sql.azurewebsites.net/todos
Method: GET
Request Body:
{
    None
}
```

#### Fetch Single Task (task 1)
```
Endpoint: http://flask-sql.azurewebsites.net/todos/{task index}
Endpoint example: http://flask-sql.azurewebsites.net/todos/1
Method: GET
Request Body:
{
    None
}
```

#### Update Task (task 1)
```
Endpoint: http://flask-sql.azurewebsites.net/todos/{task index}
Endpoint example: http://flask-sql.azurewebsites.net/todos/1
Method: PUT
Request Body:
{
    "task":"Updated task"
}
```

#### Delete Task (task 1)
```
Endpoint: http://flask-sql.azurewebsites.net/todos/{task index}
Endpoint example: http://flask-sql.azurewebsites.net/todos/1
Method: DELETE
Request Body:
{
    None
}
```

## Steps To Setup With Your Own Existing MySQL Server

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

### Setup Flask Backend

1. Install requirements

```
pip install -r requirements.txt
```
2. Create .env file and add the following code (replace {} with your MySQL configuration variables).
```
MYSQL_DATABASE_USER = "{database username}"
MYSQL_DATABASE_PASSWORD = "{database password}"
MYSQL_DATABASE_DB = "{database name}"
MYSQL_DATABASE_HOST = "{database host}"
```

3. Run

```
python api.py
```
or
```
flask run
```
4. Send requests to ```http://127.0.0.1:5000/``` instead of ```http://flask-sql.azurewebsites.net/```.


