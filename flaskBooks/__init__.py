from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

app = Flask(__name__)

#Secret key to protect against cookie editing etc
app.config['SECRET_KEY'] = '144c3171a3fdeae712ed9bd8dac5994a'
#Location for the project's SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

from flaskBooks import routes