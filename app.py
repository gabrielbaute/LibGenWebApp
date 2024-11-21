from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_mail import Mail
from flask_bcrypt import Bcrypt
from libgen_api import LibgenSearch
from loadadmin import create_admin_user
from models import db
import routes, dotenv, os

# Cargar variables de entorno
dotenv.load_dotenv()
appport = os.getenv('FLASKPORT', 5000)
dburi = os.getenv('SQLALCHEMY_DATABASE_URI', 'sqlite:///site.db')
setdebug = os.getenv('DEBUG', False)
appdomain = os.getenv('FLASK_DOMAIN')
mail_settings = {
    "MAIL_SERVER": os.getenv('MAIL_SERVER'),
    "MAIL_PORT": os.getenv('MAIL_PORT'),
    "MAIL_USE_TLS": os.getenv('MAIL_USE_TLS') == 'True',
    "MAIL_USE_SSL": os.getenv('MAIL_USE_SSL') == 'True',
    "MAIL_USERNAME": os.getenv('MAIL_USERNAME'),
    "MAIL_PASSWORD": os.getenv('MAIL_PASSWORD'),
    "MAIL_DEFAULT_SENDER": os.getenv('MAIL_DEFAULT_SENDER')
}

# Configurar Flask
app = Flask(__name__, template_folder='templates')
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
app.config['SQLALCHEMY_DATABASE_URI'] = dburi
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config.update(mail_settings)

# Inicializar extensiones
db.init_app(app)
mail = Mail(app)
bcrypt = Bcrypt(app)
search = LibgenSearch()
login_manager = LoginManager(app)

# Inicializar rutas
routes.init_routes(app, search, db, login_manager, bcrypt)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        create_admin_user()
    app.run(debug=setdebug, port=appport)
