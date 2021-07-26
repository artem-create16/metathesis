from flask import render_template, Blueprint
import os

template_dir = os.path.abspath('../templates')
error_blueprint = Blueprint('error', __name__, url_prefix='/error', template_folder=template_dir)


@error_blueprint.app_errorhandler(403)
def status_code_403(error):
    return render_template('error/error_403.html'), 403


@error_blueprint.app_errorhandler(404)
def status_code_404(error):
    return render_template('error/error_404.html'), 404
