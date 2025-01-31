'''
    Docstring
'''
# pylint: disable = C0103
import datetime
from flask import Blueprint, render_template, redirect, url_for
from Funcionario import Funcionario
from app.forms import funcionario_form
from app.models import funcionario_model
from app import db

# from app import app

cadastro_func_blueprint = Blueprint('cadastro', __name__)
listar_func_blueprint = Blueprint('funcionarios', __name__)
editar_func_blueprint = Blueprint('editar', __name__)

# Página passando valor default ou passando variavel pela rota
# @cadastro_Func_blueprint.route('/')
# @cadastro_Func_blueprint.route('/menufunc/', defaults={'nome': None})
# @cadastro_Func_blueprint.route('/menufunc/<string:nome>')
# def cadastro_func(nome):
#     ''' Docstring'''
#     if nome:
#         return render_template('menuCadastro.html', nome=nome)
#     return render_template('menuCadastro.html', nome='Nome Funcionario')


# @cadastro_add_blueprint.route('/menufunc/addfunc/', methods=['GET', 'POST'])
# def cadastro_add():
#     ''' Docstring'''
#     if request.method == 'POST':
#         newfunc = Funcionario(request.form['empresa'])
#         newfunc.set_nome(request.form['nome'])
#         newfunc.set_cpf(request.form['cpf'])
#         # empresa = request.form['empresa']
#         # funcao = request.form['funcao']
#         print([newfunc.get_nome(), newfunc.get_cpf()])
#         # return f'<h1> nome: {nome}</h1> <h1> CPF: {cpf}</h1>'
#         # return redirect('/menufunc/')
#         return redirect(url_for('menufunc.cadastro_func'))
#     return render_template('cadastro_add.html')

@listar_func_blueprint.route('/funcionarios/', defaults={'idd': None}, methods=['GET', 'POST'])
@listar_func_blueprint.route('/funcionarios/<int:idd>/')
def listar_func(idd):
    '''docstring'''
    if idd is not None:
        print(idd)
        func = funcionario_model.func_model.query.filter_by(id=idd).first()
        # func.data_nasc = datetime.date.strftime(func.data_nasc, "%d/%m/%Y")
        return render_template("funcionarios/func_perfil.html/", funcionarios=func)
    func = funcionario_model.func_model.query.all()
    return render_template("/funcionarios/func_cadastrados.html/", funcionarios=func)


@editar_func_blueprint.route("/funcionarios/editar/<int:idd>/", methods=['GET', 'POST'])
def editar_func(idd):
    '''docstring'''
    func = funcionario_model.func_model.query.filter_by(id=idd).first()
    form = funcionario_form.funcionario_Form(obj=func)
    if form.validate_on_submit():
        editfunc = Funcionario(form.empresa.data)
        editfunc.set_nome(form.nome.data)
        editfunc.set_sexo(form.sexo.data)
        editfunc.set_data_nasc(form.data_nasc.data)
        editfunc.set_cpf(form.cpf.data)
        editfunc.set_empresa(form.empresa.data)
        editfunc.set_cargo(form.cargo.data)
        editfunc.set_email(form.email.data)

        func.nome = editfunc.get_nome()
        func.sexo = editfunc.get_sexo()
        func.data_nasc = datetime.date.strftime(
            editfunc.get_data_nasc(), "%d/%m/%Y")
        func.cpf = editfunc.get_cpf()
        func.empresa = editfunc.get_empresa()
        func.cargo = editfunc.get_cargo()
        func.email = editfunc.get_email()

        try:
            db.session.commit()
        except NameError as db_error:
            print(f"cliente nao foi editado no BD type:{db_error}")
        return redirect(url_for('funcionarios.listar_func'))
    return render_template("/funcionarios/form.html", form=form)


@cadastro_func_blueprint.route("/funcionarios/cadastrar_func/", methods=['GET', 'POST'])
def cadastrar_func():
    '''docstring'''
    form = funcionario_form.funcionario_Form()
    if form.validate_on_submit():
        newfunc = Funcionario(form.empresa.data)
        newfunc.set_nome(form.nome.data)
        newfunc.set_sexo(form.sexo.data)
        newfunc.set_data_nasc(form.data_nasc.data)
        newfunc.set_cpf(form.cpf.data)
        newfunc.set_empresa(form.empresa.data)
        newfunc.set_cargo(form.cargo.data)
        newfunc.set_email(form.email.data)

        data_formatada = datetime.date.strftime(
            newfunc.get_data_nasc(), "%d/%m/%Y")

        func = funcionario_model.func_model(
            nome=newfunc.get_nome(), sexo=newfunc.get_sexo(),
            data_nasc=data_formatada, cpf=newfunc.get_cpf(),
            empresa=newfunc.get_empresa(), cargo=newfunc.get_cargo(),
            email=newfunc.get_email())
        try:
            db.session.add(func)
            db.session.commit()
        except NameError as db_error:
            print(f"cliente nao foi cadastrado no BD type:{db_error}")
        return redirect(url_for('funcionarios.listar_func'))
    return render_template('/funcionarios/form.html', form=form)
