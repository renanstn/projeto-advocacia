from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from shared.db import db

def create_app():

    app = Flask(__name__)

    app.config.from_pyfile('config.py')

    with app.app_context():
        print('passou aqui')
        db.init_app(app)
        db.create_all()
    
    login_manager = LoginManager()
    # login_manager.login_view('auth.login')
    login_manager.init_app(app)

    from models.usuarios import Usuarios

    @login_manager.user_loader
    def load_user(user_id):
        return Usuarios.query.get(int(user_id))

    # Blueprints
    from auth.auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    return app