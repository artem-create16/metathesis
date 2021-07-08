import os

import flask_login
from dotenv import load_dotenv
from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy


load_dotenv()

db = SQLAlchemy()
migrate = Migrate()
login_manager = flask_login.LoginManager()


def init_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = str(os.getenv("SECRET_KEY"))
    app.config['SQLALCHEMY_DATABASE_URI'] = str(os.getenv("SQLALCHEMY_DATABASE_URI"))
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    with app.app_context():
        from application.main.routes import main_blueprint
        from application.auth.routes import auth_blueprint
        from application.models import User, Product, ProductPhoto
        app.register_blueprint(main_blueprint)
        app.register_blueprint(auth_blueprint)
        # commands
        from application.core.commands import seed_db
        app.cli.add_command(seed_db)

    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)

    return app
