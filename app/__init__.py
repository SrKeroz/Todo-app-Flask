from flask import Flask
from flask_bootstrap import Bootstrap
from .config import Config
from auth import auth
from flask_login import LoginManager
from .models import UserModel


login_manager = LoginManager()
login_manager.login_view = "auth.login"

@login_manager.user_loader
def load_user(username):
    return UserModel.query(username)
# Con esto logre solucionar el error que me marcaba. 
# flask-login:Exception: No user_loader has been installed for this LoginManager.
#  Add one with the ‘LoginManager.user_loader’ decorator




def create_app():
    app = Flask(__name__)
    bootstrap = Bootstrap(app)

    app.config.from_object(Config)

    login_manager.init_app(app)

    app.register_blueprint(auth)

    return app