# Flask-REST-API-Python-MySQL

### What is this project?

- This is a REST API backend built using Flask and MySQL.
- Users can perform C.R.U.D. operations on a todolist MySQL database table.

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

### API Setup and Use

1. Install requirements

```
pip install -r requirements.txt
```

2. Run

```
python api.py
```

3. Send raw JSON requests to http://127.0.0.1:5000/todos (examples can be found in tests folder)
