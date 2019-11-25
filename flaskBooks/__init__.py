from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

#Secret key to protect against cookie editing etc
app.config['SECRET_KEY'] = '144c3171a3fdeae712ed9bd8dac5994a'
#Location for the project's SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

from flaskBooks import routes