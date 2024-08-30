# app/forms.py
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired

class NameForm(FlaskForm):
    name = StringField('Cadastre o novo Professor:', validators=[DataRequired()])
    role = SelectField('Disciplina associada:', choices=[], validators=[DataRequired()])
    submit = SubmitField('Cadastrar')
