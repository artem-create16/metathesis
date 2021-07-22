import os

from flask import Blueprint
from flask_restful import abort, Resource

from application.models import Ad

template_dir = os.path.abspath('../templates')

api_blueprint = Blueprint('api', __name__, template_folder=template_dir)


class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}


def abort_if_ad_doesnt_exist(ad_id):
    abort(404, message="Ad {} doesn't exist".format(ad_id))


class AdApi(Resource):
    def get(self, ad_id):
        ad = Ad.query.get(ad_id)
        if not ad:
            abort_if_ad_doesnt_exist(ad_id)
        else:
            blank = {
                'id': str(ad.id),
                'title': str(ad.title),
                'description': str(ad.description),
                'category': str(ad.category),
                'user_id': str(ad.user_id)
            }
            return blank
