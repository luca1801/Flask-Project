'''
docstring que o pylint exige
'''
# pylint: disable=C0116,C0303,C0301,C0103, C0116, R0903

from app.views.Funcionarios import cadastro_func_blueprint
from app.views.Funcionarios import listar_func_blueprint
from app.views.Funcionarios import editar_func_blueprint
# from app.views.usuarios_view import usuarios_blueprint
from app import app
# from src.app.views.perfil_view import usuarios_blueprint


# app.register_blueprint(usuarios_blueprint)
app.register_blueprint(cadastro_func_blueprint)
app.register_blueprint(editar_func_blueprint)
app.register_blueprint(listar_func_blueprint)

if __name__ == '__main__':
    app.run()
    # app.run(host='0.0.0.0', port=5000)
