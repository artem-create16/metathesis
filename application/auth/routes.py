import os

from flask import Blueprint
import application.auth.controller as controller

template_dir = os.path.abspath('../templates')
auth_blueprint = Blueprint('auth', __name__, url_prefix='/auth', template_folder=template_dir)


@auth_blueprint.route('/signin', methods=['GET', 'POST'])
def sign_in():
    return controller.sign_in()


@auth_blueprint.route('/signup', methods=['GET', 'POST'])
def sign_up():
    return controller.sign_up()


@auth_blueprint.route('/signout', methods=['GET'])
def sign_out():
    return controller.sign_out()
