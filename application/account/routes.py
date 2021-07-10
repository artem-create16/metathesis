import os

from flask import Blueprint
from flask_login import login_required

import application.account.controller as controller

template_dir = os.path.abspath('../templates')
account_blueprint = Blueprint('account', __name__, url_prefix='/account', template_folder=template_dir)


@account_blueprint.route('/account/<user_id>', methods=['GET', 'POST'])
@login_required
def show_account(user_id):
    controller.show_account(user_id)


@account_blueprint.route('/my-account', methods=['GET', 'POST'])
@login_required
def show_my_account():
    return controller.show_my_account()

