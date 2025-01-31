'''docstring'''
# pylint: disable=C0103

from flask_wtf import FlaskForm
from wtforms import StringField, DateField, SelectField
from wtforms.fields import EmailField
from wtforms.validators import DataRequired, Email
DATE_INPUT_FORMATS = ['%d-%m-%Y', '%Y-%m-%d']


class funcionario_Form(FlaskForm):
    '''docstring'''
    nome = StringField("nome", validators=[DataRequired()])
    email = EmailField("email", validators=[Email(), DataRequired()])
    data_nasc = DateField("data_nasc", validators=[
                          DataRequired()])
    sexo = SelectField("sexo", validators=[DataRequired()],
                       choices=[('F', 'Feminino'), ('M', 'Masculino')])
    empresa = StringField("empresa", validators=[DataRequired()])
    cpf = StringField("cpf", validators=[DataRequired()])
    cargo = StringField("cargo", validators=[DataRequired()])
