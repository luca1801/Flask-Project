'''
    Docstring
'''
# pylint: disable = C0103
import datetime
from flask import Blueprint, render_template, redirect, url_for, request, current_app, flash
# from flask_wtf.csrf import generate_csrf

from app.entity.Funcionario import Funcionario

from app.forms import funcionario_form
from app.models import funcionario_model
from app.services import func_service
# from app import db


# from app import app

cadastro_func_blueprint = Blueprint('cadastro', __name__)
listar_func_blueprint = Blueprint('funcionarios', __name__)
editar_func_blueprint = Blueprint('editar', __name__)
remover_func_blueprint = Blueprint('remover', __name__)


@listar_func_blueprint.route('/funcionarios/', defaults={'idd': None}, methods=['GET', 'POST'])
@listar_func_blueprint.route('/funcionarios/<int:idd>/')
def listar_func(idd):
    '''Listar funcionarios or show details of a specific funcionario by id.'''
    # func.data_nasc = datetime.date.strftime(func.data_nasc, "%d/%m/%Y")
    try:
        current_app.logger.info("View: user acessed listar_func")
        # func by ID
        if idd is not None:
            func = func_service.list_func_id(idd)
            if func is None:
                flash("Funcionario não encontrado", 'error')
                return redirect(url_for('funcionarios.listar_func'))
            return render_template("funcionarios/func_perfil.html/", funcionarios=func)
        # all func
        func = func_service.list_func()
        return render_template("/funcionarios/func_cadastrados.html/", funcionarios=func)
    except NameError as error:
        current_app.logger.error(f"View: Error fetching funcionarios: {error}")
        flash("An error occurred while fetching funcionarios", "error")
        return redirect(url_for('listar_func'))


@editar_func_blueprint.route("/funcionarios/editar/<int:idd>/", methods=['GET', 'POST'])
def editar_func(idd):
    '''Edit details of a specific funcionario by id.'''
    try:
        func = func_service.list_func_id(idd)
        print(func)
        if func is None:
            flash("Funcionario not Found", 'error')
            return redirect(url_for('funcionarios.listar_func'))
        form = funcionario_form.funcionario_Form(obj=func)
        form.sexo.data = func.sexo
        if form.validate_on_submit():
            form.populate_obj(func)
            try:
                func_service.edit_func(func)
                flash("funcionario editado com sucesso", "success")
            except NameError as error:
                flash("um erro ocorreu enquando editava funcionário", "error")
                current_app.logger.error(
                    f"View: Error editing funcionario: {error}")
            return redirect(url_for('funcionarios.listar_func'))
        return render_template("/funcionarios/form.html", form=form)
    except NameError as error:
        flash("um erro ocorreu enquando editava funcionário", "error")
        current_app.logger.error(f"View: Error editing funcionario: {error}")
        return redirect(url_for('listar_func'))


@cadastro_func_blueprint.route("/funcionarios/register_func/", methods=['GET', 'POST'])
def register_func():
    ''' register new funcionario'''
    form = funcionario_form.funcionario_Form()
    if form.validate_on_submit():
        try:
            newfunc = Funcionario(form.empresa.data, form.nome.data, form.email.data,
                                  form.data_nasc.data, form.sexo.data, form.cargo.data,
                                  form.cpf.data)
            data_formatada = datetime.date.strftime(
                newfunc.get_data_nasc(), "%d/%m/%Y")

            func = funcionario_model.func_model(
                nome=newfunc.get_nome(), sexo=newfunc.get_sexo(),
                data_nasc=data_formatada, cpf=newfunc.get_cpf(),
                empresa=newfunc.get_empresa(), cargo=newfunc.get_cargo(),
                email=newfunc.get_email())

            func_service.register_func(func)
            flash("Funcionario cadastrado com sucesso!", "success")
        except NameError as error:
            flash("Erro ao cadastrar funcionario.", "error")
            current_app.logger.error(
                f"View: Error registering funcionario: {error}")
        return redirect(url_for('funcionarios.listar_func'))
    return render_template('/funcionarios/form.html', form=form)


@remover_func_blueprint.route("/funcionarios/remover/<int:idd>", methods=['GET', 'POST'])
def remover_func(idd):
    ''' Removing a specific funcionario by id.'''
    func = func_service.list_func_id(idd)
    if func is None:
        flash("Funcionario não encontrado.", "error")
        return redirect(url_for('funcionarios.listar_func'))
    if request.method == 'POST':
        csrf_token = request.form.get('csrf_token')
        if not csrf_token:
            current_app.logger.warning('View: CSRF token missing or incorrect')
            flash('CSRF token missing or incorrect', 'error')
        try:
            func_service.remove_func(func)
            flash("Funcionario removido com sucesso!", "success")
        except NameError as error:
            flash("Erro ao remover funcionario", "error")
            current_app.logger.error(
                f"View: Error deleting funcionario: {error}")
        return redirect(url_for('funcionarios.listar_func'))
    return render_template('/funcionarios/remover_func.html/', funcionarios=func)
