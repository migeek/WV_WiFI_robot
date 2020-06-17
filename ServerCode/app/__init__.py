""" This folder tells python that this folder should be treated as a package """
from flask import Flask
from config import Config
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_socketio import SocketIO

# __name__ for __init__.py file is the parent folder
app_instance=Flask(__name__)

app_instance.config.from_object(Config)
db = SQLAlchemy(app=app_instance)
migrate = Migrate(app=app_instance, db=db)
login = LoginManager(app=app_instance)
login.login_view = 'login' # for login view name

sio = SocketIO(app_instance)

# From our app package import routes
from app import routes, models, events

