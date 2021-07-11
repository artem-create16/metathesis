import os

from flask import Blueprint
from flask_login import login_required

import application.ad.controller as controller


template_dir = os.path.abspath('../templates')
ad_blueprint = Blueprint('ad', __name__, url_prefix='/ad', template_folder=template_dir)


@ad_blueprint.route('/create-ad', methods=['GET', 'POST'])
@login_required
def create_ad():
    return controller.create_ad()


@ad_blueprint.route('/upload/<ad_id>', methods=['GET', 'POST'])
@login_required
def upload_photo(ad_id):
    return controller.upload_photo(ad_id)


@ad_blueprint.route('/<ad_id>')
@login_required
def show_ad(ad_id):
    return controller.show_ad(ad_id)


@ad_blueprint.route('/<ad_id>/edit', methods=['GET', 'POST'])
@login_required
def edit_ad(ad_id):
    return controller.edit_ad(ad_id)


@ad_blueprint.route('/<ad_id>/delete')
@login_required
def delete_ad(ad_id):
    return controller.delete_ad(ad_id)
