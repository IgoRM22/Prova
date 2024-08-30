# app/routes.py
from flask import render_template, session, redirect, url_for, flash, request
from . import db
from .models import User, Role
from .forms import NameForm
from flask import Blueprint

main = Blueprint('main', __name__)

@main.route('/')
def index():
    users = User.query.all()
    return render_template('disciplinas.html', users=users)

@main.route('/professores', methods=['GET', 'POST'])
def professores():
    form = NameForm()  # Substitua por um formulário específico para professores, se existir

    if form.validate_on_submit():
        user = User(username=form.name.data)
        db.session.add(user)
        db.session.commit()
        flash('Professor cadastrado com sucesso!')
        return redirect(url_for('main.professores'))

    users = User.query.all()
    return render_template('professores.html', form=form, users=users)

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
