import os

from flask import Blueprint, render_template, request

from application.models import Ad
from application.models import Categories


template_dir = os.path.abspath('../templates')
main_blueprint = Blueprint('main', __name__, template_folder=template_dir)


@main_blueprint.route('/')
def index():
    page = request.args.get('page')
    if page and page.isdigit():
        page = int(page)
    else:
        page = 1
    search = request.args.get('search')
    categories = request.args.getlist('category')
    if search:
        search = "%{}%".format(search)
        ads = Ad.query.filter(
            Ad.title.like(search) |
            Ad.category.like(search) |
            Ad.description.like(search)
        ).order_by(Ad.created_at.desc())

    if categories:
        ads = Ad.query.filter(
            Ad.category.in_(categories)
        ).all()

    else:
        ads = Ad.query.filter().order_by(Ad.created_at.desc())

    pages = ads.paginate(page=page, per_page=5)

    return render_template('main/main.html', title='Index',
                           ads=ads, categoryes=Categories, pages=pages)
