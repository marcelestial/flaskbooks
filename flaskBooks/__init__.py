from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import desc
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__)

#Secret key to protect against cookie editing etc
app.config['SECRET_KEY'] = '144c3171a3fdeae712ed9bd8dac5994a'
#Location for the project's SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'

from flaskBooks import routes