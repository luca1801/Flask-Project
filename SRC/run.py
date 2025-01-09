'''
docstring que o pylint exige
'''
# pylint: disable=C0116,C0303,C0301,C0103, C0116

from app import app
# from src.app.views.perfil_view import usuarios_blueprint

# app.register_blueprint('usuarios_blueprint')
from app.views.usuarios_view import usuarios_blueprint
from app.views.cadastro_func import cadastro_Func_blueprint
from app.views.cadastro_func import cadastro_add_blueprint

app.register_blueprint(usuarios_blueprint)
app.register_blueprint(cadastro_Func_blueprint)
app.register_blueprint(cadastro_add_blueprint)

if __name__ == '__main__':
    app.run(debug=True)
