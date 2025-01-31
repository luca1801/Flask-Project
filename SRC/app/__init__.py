''' documentation'''
# pylint: disable= C0413, C0103

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_wtf import CSRFProtect
from flask_babel import Babel


app = Flask(__name__)

app.config.from_object('config')

# engine   = create_engine(SQLALCHEMY_DATABASE_URI)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
csrf = CSRFProtect(app)
csrf.init_app(app)

#ativando pacote de traducao do erros
babel = Babel(app)

from .models import funcionario_model
# from .views import cadastro_func
# from .views import perfil_view
