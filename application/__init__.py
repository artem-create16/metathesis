import os

import flask_login
from dotenv import load_dotenv
from flask import Flask
from flask_migrate import Migrate
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from flask_admin import Admin

load_dotenv()

db = SQLAlchemy()
migrate = Migrate()
login_manager = flask_login.LoginManager()
# api = Api()


def init_app():
    app = Flask(__name__)
    UPLOAD_FOLDER = 'static/uploads/'
    app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
    app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024
    app.config['SECRET_KEY'] = str(os.getenv("SECRET_KEY"))
    app.config['SQLALCHEMY_DATABASE_URI'] = str(os.getenv("SQLALCHEMY_DATABASE_URI"))
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    with app.app_context():
        from application.main.routes import main_blueprint
        from application.auth.routes import auth_blueprint
        from application.ad.routes import ad_blueprint
        from application.account.routes import account_blueprint
        from application.error.routes import error_blueprint
        from application.models import User, Ad, AdPhoto
        from application.api.routes import AdApi
        from application.api.routes import api_blueprint
        from .admin import AdminView, HomeAdminView

        app.register_blueprint(main_blueprint)
        app.register_blueprint(auth_blueprint)
        app.register_blueprint(ad_blueprint)
        app.register_blueprint(account_blueprint)
        app.register_blueprint(error_blueprint)
        app.register_blueprint(api_blueprint)
        # commands
        from application.core.commands import seed_db
        app.cli.add_command(seed_db)
        # api
        api = Api(app)

    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)
    admin = Admin(app, name='Metathesis', url='/', index_view=HomeAdminView(name=''))

    admin.add_view(AdminView(User, db.session, name='Users',
                             endpoint='User'))
    admin.add_view(AdminView(Ad, db.session, name='Ads',
                             endpoint='Project'))
    # registration api link
    api.add_resource(AdApi, '/api/ad/<ad_id>')

    return app
