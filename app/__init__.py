from flask import Flask
from config import config_options
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy

bootstrap = Bootstrap()
db = SQLAlchemy()

def create_app(config_name):
    # Initializing application
    app = Flask(__name__)

    # creating app configurations
    app.config.from_object(config_options[config_name])


    #initializing flask extensions
    bootstrap.init_app(app)
    db.init_app(app)

    # registering a blueprint
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    #Setting config
    from .request import configure_request
    configure_request(app)


    # from app import views
    # from app import error

    return app