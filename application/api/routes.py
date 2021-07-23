import os

from flask import Blueprint
from flask_restful import abort, Resource, reqparse

from application import db
from application.models import Ad


template_dir = os.path.abspath('../templates')

api_blueprint = Blueprint('api', __name__, template_folder=template_dir)


parser = reqparse.RequestParser()
parser.add_argument('category', type=str, required=True)
parser.add_argument('title', type=str, required=True)
parser.add_argument('description', type=str, required=True)
parser.add_argument('user_id', type=int, required=True)


def create_json(ad):
    blank = {
        'id': str(ad.id),
        'title': str(ad.title),
        'description': str(ad.description),
        'category': str(ad.category),
        'user_id': str(ad.user_id)
    }
    return blank


def create_ad():
    args = parser.parse_args()
    new_ad = Ad(
        category=args['category'],
        title=args['title'],
        description=args['description'],
        user_id=args['user_id']
    )
    db.session.add(new_ad)
    db.session.commit()
    return create_json(new_ad)


class AdApi(Resource):
    def get(self, ad_id):
        """
        curl http://localhost/api/ad/54
        """
        ad = Ad.query.get(ad_id)
        if not ad:
            abort(404, message="Ad {} doesn't exist".format(ad_id))
        return create_json(ad)

    def delete(self, ad_id):
        """
        curl http://localhost/api/ad/1 -X DELETE -v
        """
        ad = Ad.query.get(ad_id)
        if not ad:
            abort(404, message=f"Ad {ad_id} doesn't exist")
        db.session.delete(ad)
        db.session.commit()
        return f'Ad {ad_id} was deleted'

    def put(self, ad_id):
        ad = Ad.query.get(ad_id)
        if ad:
            abort(409, message=f"Ad {ad_id} already exists")
        return create_ad()

    def patch(self, ad_id):
        """
        curl --request PATCH http://localhost/api/ad/54 -d "category=transport&title=title19.56&description=description_new&user_id=1" -v
        """
        ad = Ad.query.get(ad_id)
        if not ad:
            abort(404, message=f"Ad {ad_id} doesn't exist")
        args = parser.parse_args()
        if args['category']:
            ad.category = args['category']
        if args['title']:
            ad.title = args['title']
        if args['description']:
            ad.description = args['description']
        if args['user_id']:
            ad.user_id = args['user_id']
        db.session.commit()

        return create_json(ad)



class AdPostApi(Resource):
    def post(self):
        return create_ad()

