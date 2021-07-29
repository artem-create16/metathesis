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
    page = request.args.get('page')
    ads = Ad.query.order_by(Ad.created_at.desc())
    if page and page.isdigit():
        page = int(page)
    else:
        page = 1

    if search:
        found = "%{}%".format(search)
        ads = Ad.query.filter(
            Ad.title.like(found) |
            Ad.category.like(found) |
            Ad.description.like(found)
        ).order_by(Ad.created_at.desc())

    if categories:
        ads = Ad.query.filter(
            Ad.category.in_(categories)
        )
    pages = ads.paginate(page=page, per_page=5)

    return render_template('main/main.html', title='Index',
                           ads=ads, categoryes=Categories, pages=pages)
