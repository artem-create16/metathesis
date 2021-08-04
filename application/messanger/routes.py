import os

from flask import Blueprint
from flask_login import login_required

import application.messanger.controller as controller

template_dir = os.path.abspath('../templates')
messenger_blueprint = Blueprint('messenger', __name__, url_prefix='/messenger', template_folder=template_dir)


@messenger_blueprint.route('/message/<ad_id>', methods=['GET', 'POST'])
@login_required
def main(ad_id):
    return controller.main(ad_id)


@messenger_blueprint.route('/my_messages')
@login_required
def my_messages():
    return controller.my_messages()


