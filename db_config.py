from app import app
from flaskext.mysql import MySQL
from dotenv import load_dotenv
import os
load_dotenv()
mysql = MySQL()

# MySQL configurations
app.config['MYSQL_DATABASE_USER'] = os.getenv("MYSQL_DATABASE_USER")
app.config['MYSQL_DATABASE_PASSWORD'] = "adminpassword1"
app.config['MYSQL_DATABASE_DB'] = "todolist"
app.config['MYSQL_DATABASE_HOST'] = "database-1.cclou8jjrcwz.us-west-2.rds.amazonaws.com"

mysql.init_app(app)


