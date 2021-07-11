import os

from flask import Blueprint, render_template, request
from application.models import Ad

template_dir = os.path.abspath('../templates')
main_blueprint = Blueprint('main', __name__, template_folder=template_dir)


@main_blueprint.route('/')
def index():
    ads = Ad.query.filter().order_by(Ad.created_at.desc()).all()
    return render_template('main/main.html', title='Index',
                           ads=ads)
