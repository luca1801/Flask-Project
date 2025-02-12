'''  service for manipulate data from funcionario_model  '''

from flask import current_app
from app.models import funcionario_model
from app import db


def list_func():
    '''List all funcionarios.'''
    try:
        current_app.logger.info("Services: Fetching all funcionarios")
        func = funcionario_model.func_model.query.all()
        return func
    except NameError as db_error:
        current_app.logger.error(f"Services: Error fetching all funcionarios: {db_error}")
        return None

def list_func_id(idd):
    '''List funcionario by id.'''
    try:
        current_app.logger.info(
                f"Service: Fetching details for funcionario with id: {idd}")
        func = funcionario_model.func_model.query.filter_by(id=idd).first()
        if func is None:
            current_app.logger.warning(
                    f"Services: funcionario with id: {idd} not found")
        return func
    except NameError as db_error:
        current_app.logger.error(f"Services: Error fetching funcionarios idd: {idd} {db_error}")
        return None

def register_func(func):
    '''Register a new funcionario.'''
    try:
        current_app.logger.info("Services: Registering new funcionario")
        db.session.add(func)
        db.session.commit()
        current_app.logger.info(
                f"Services: Funcionario {func.nome} cadastrado com sucesso.")
    except NameError as db_error:
        db.session.rollback()
        current_app.logger.error(f"Services: Error registering funcionario: {db_error}")

def edit_func(func):
    '''Edit details of a specific funcionario.'''
    try:
        current_app.logger.info(
                f"Services: Editing details for funcionario with id: {func.id}")
        db.session.commit()
        current_app.logger.info(
                f"Services: Funcionario {func.nome} sucessfully edited.")
    except NameError as db_error:
        db.session.rollback()
        current_app.logger.error(f"Services: Error editing funcionario: {db_error}")

def remove_func(func):
    '''Remove a specific funcionario.'''
    try:
        current_app.logger.info(
                f"Services: Removing funcionario with id: {func.id}")
        db.session.delete(func)
        db.session.commit()
        current_app.logger.info(
                f"Services: Funcionario {func.nome} sucessfully removed.")
    except NameError as db_error:
        db.session.rollback()
        current_app.logger.error(f"Services: Error removing funcionario: {db_error}")
