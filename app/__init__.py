# app/__init__.py

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from config import config

# Instancia as extensões
db = SQLAlchemy()
bootstrap = Bootstrap()

def create_app(config_name='default'):
    # Cria a instância da aplicação Flask
    app = Flask(__name__)

    # Aplica as configurações
    app.config.from_object(config[config_name])

    # Inicializa as extensões com a aplicação
    db.init_app(app)
    bootstrap.init_app(app)

    # Registra o blueprint principal
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app
