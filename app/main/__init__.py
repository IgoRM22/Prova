# app/main/__init__.py

from flask import Blueprint

# Cria o blueprint
main = Blueprint('main', __name__)

# Importa as rotas para registrar no blueprint
from . import routes
