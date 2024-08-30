from flask import render_template, session, redirect, url_for
from . import main
from .forms import NameForm
from .. import db
from ..models import User, Role

@main.route('/', methods=['GET', 'POST'])
def index():
    form = NameForm()

    # Preenche as opções do campo de função dinamicamente
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
        return redirect(url_for('.index'))

    users = User.query.all()
    roles = Role.query.all()

    return render_template('index.html', form=form, name=session.get('name'),
                           known=session.get('known', False), user_all=users, roles=roles)
