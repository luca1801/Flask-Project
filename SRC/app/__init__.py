''' documentation'''
# pylint: disable= C0413, C0103

import logging
from flask import Flask, has_request_context, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_wtf import CSRFProtect
from flask_babel import Babel

#config logging
class RequestFormatter(logging.Formatter):
    '''using custom formatter to inject contextual data into logging'''
    def format(self, record):
        if has_request_context():
            record.url = request.url
            record.remote_addr = request.remote_addr
        else:
            record.url = None
            record.remote_addr = None
        return super().format(record)

# create a formatter object
logformatter = RequestFormatter(
            '[%(asctime)s] %(remote_addr)s requested %(url)s\n'
            '%(levelname)s in %(module)s: %(message)s')

# get the root logger
logger = logging.getLogger()

# add console handler to the root logger
consoleHandler = logging.StreamHandler()
consoleHandler.setFormatter(logformatter)
logger.addHandler(consoleHandler)

# add file handler to the root logger
fileHandler = logging.FileHandler("src/logs/logs.log")
fileHandler.setFormatter(logformatter)
logger.addHandler(fileHandler)

#logging.basicConfig(filename="src/logs/logs.log", level=logging.INFO)

app = Flask(__name__)

app.config.from_object('config')
# pp.config['SECRET_KEY'] = 'your-secret-key'

# engine   = create_engine(SQLALCHEMY_DATABASE_URI)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
csrf = CSRFProtect(app)
csrf.init_app(app)

# ativando pacote de traducao do erros
babel = Babel(app)

from .models import funcionario_model  # ficar abaixo de app
# from .views import cadastro_func
# from .views import perfil_view
