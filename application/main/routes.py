import os

from flask import Blueprint, render_template, request


template_dir = os.path.abspath('../templates')
main_blueprint = Blueprint('main', __name__, template_folder=template_dir)


@main_blueprint.route('/')
def index():
    return render_template('main/main.html', title='Index')
