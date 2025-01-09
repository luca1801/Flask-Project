'''
    Docstring
'''
from flask import Blueprint, render_template, request, redirect
from Funcionario import Funcionario

cadastro_Func_blueprint = Blueprint('/menucadastro/', __name__)
cadastro_add_blueprint = Blueprint('/menufunc/add/', __name__)


@cadastro_Func_blueprint.route('/menufunc/')
def cadastro_func():
    ''' Docstring'''
    return render_template('menuCadastro.html')


@cadastro_add_blueprint.route('/menufunc/add/', methods=['GET', 'POST'])
def cadastro_add():
    ''' Docstring'''
    if request.method == 'POST':
        newfunc = Funcionario(request.form['empresa'])
        newfunc.set_nome(request.form['nome'])
        newfunc.set_cpf(request.form['cpf'])
        #empresa = request.form['empresa']
        #funcao = request.form['funcao']
        print([newfunc.get_nome(), newfunc.get_cpf()])
        #return f'<h1> nome: {nome}</h1> <h1> CPF: {cpf}</h1>'
        return redirect('/menufunc/')
    return render_template('cadastro_add.html')
