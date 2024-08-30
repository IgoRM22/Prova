import os
from app import create_app, db
from app.models import User, Role
from flask_migrate import MigrateCommand
from flask_script import Manager

# Cria a aplicação com base na configuração especificada
app = create_app(os.getenv('FLASK_CONFIG') or 'default')
manager = Manager(app)

# Comando para iniciar o shell com o contexto da aplicação
@manager.command
def shell():
    return dict(app=app, db=db, User=User, Role=Role)

if __name__ == '__main__':
    manager.run()
