import os

from flask import Blueprint, render_template, request

from application.models import Ad
from application.models import Categories


template_dir = os.path.abspath('../templates')
main_blueprint = Blueprint('main', __name__, template_folder=template_dir)


@main_blueprint.route('/')
def index():
    search = request.args.get('search')
    categories = request.args.getlist('category')
    print("Categories -->", categories, flush=True)
    if search:
        ads = Ad.query.filter(
            Ad.title.contains(search) |
            Ad.category.contains(search) |
            Ad.description.contains(search)
        ).order_by(Ad.created_at.desc()).all()

    elif categories:
        ads = Ad.query.filter(
            Ad.category.in_(categories)
        ).all()

    else:
        ads = Ad.query.filter().order_by(Ad.created_at.desc()).all()

    return render_template('main/main.html', title='Index',
                           ads=ads, categoryes=Categories)
