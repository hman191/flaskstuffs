from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
from flask_login import LoginManager

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = str(os.getenv('DATABASE_URI'))
db = SQLAlchemy(app)

app.config['SECRET_KEY'] = str(os.getenv('MY_SECRET_KEY'))

login_manager = LoginManager(app)
login_manager.login_view = 'login'

from flask_bcrypt import Bcrypt

bcrypt = Bcrypt(app)

from application import routes

