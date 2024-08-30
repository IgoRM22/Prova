# flasky.py

from app import create_app, db
from flask_migrate import Migrate

# Cria a instância da aplicação usando a factory pattern
app = create_app()

# Configura a migração do banco de dados
migrate = Migrate(app, db)

if __name__ == '__main__':
    # Inicia o servidor Flask
    app.run(debug=True)
