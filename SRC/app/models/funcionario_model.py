'''Docstring'''
# pylint: disable = C0103, R0903

from sqlalchemy_utils import ChoiceType
from app import db
# from Funcionario import Funcionario


class func_model(db.Model):
    '''Docstring'''
    __tablename__ = 'Funcionarios'

    SEXO_CHOICES = [
        ('M', 'Masculino'),
        ('F', 'Feminino')
    ]

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(50))
    sexo = db.Column(ChoiceType(SEXO_CHOICES))
    data_nasc = db.Column(db.DateTime)
    cpf = db.Column(db.String(100), unique=True)
    empresa = db.Column(db.String(50))
    cargo = db.Column(db.String(50))
    email = db.Column(db.String(200), unique=True)

    def teste(self):
        '''docstring'''
