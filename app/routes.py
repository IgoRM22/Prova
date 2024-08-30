from flask import render_template, session, redirect, url_for, flash, request
from . import db
from .models import User, Role
from .forms import NameForm  # Substitua pelo formulário específico para professores, se existir
from flask import Blueprint

main = Blueprint('main', __name__)

@main.route('/')
def index():
    users = User.query.all()
    return render_template('index.html', users=users)

@main.route('/professores', methods=['GET', 'POST'])
def professores():
    form = NameForm()

    form.role.choices = [(role.id, role.name) for role in Role.query.order_by('name')]

    if form.validate_on_submit():
        role = Role.query.filter_by(id=form.role.data).first()
        user = User.query.filter_by(username=form.name.data).first()

        if user is None:
            user = User(username=form.name.data, role=role)
            db.session.add(user)
            db.session.commit()
            session['known'] = False
        else:
            session['known'] = True

        session['name'] = form.name.data
        session['role'] = role.name
        return redirect(url_for('main.professores'))

    users = User.query.all()
    roles = Role.query.all()

    return render_template('professores.html', form=form, name=session.get('name'),
                           known=session.get('known', False), user_all=users, roles=roles)

@main.route('/disciplinas')
def disciplinas():
    users = User.query.all()
    return render_template('disciplinas.html', users=users)

@main.route('/alunos')
def alunos():
    roles = Role.query.all()
    return render_template('alunos.html', roles=roles)

@main.app_errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@main.app_errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500
