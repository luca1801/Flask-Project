'''docstring'''

from flask import Blueprint, render_template
# from app import app

usuarios_blueprint = Blueprint('usuarios', __name__)


@usuarios_blueprint.route('/usuarios/')
def lista_usuarios():
    '''docstring'''
    return render_template('usuarios_temp.html')


@usuarios_blueprint.route('/usuarios/settings/')
def usuarios_settings():
    '''docstring'''
    return render_template('usuarios_settings.html')
