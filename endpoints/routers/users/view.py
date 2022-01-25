from flask_restful import Resource, reqparse, request
from flask_restful import fields, marshal_with, marshal
from .model import User
from endpoints import DB


## Schema definition 
user_fields = {
    'id': fields.Integer,
    'name': fields.String,
    'email': fields.String,
}

user_list_fields = {
    'count': fields.Integer,
    'users': fields.List(fields.Nested(user_fields)),
}


## Create View Endpoint
class UserResource(Resource):
    user_post_parser = reqparse.RequestParser()
    user_post_parser.add_argument('name', type=str, required=True, help='name parameter is required')
    user_post_parser.add_argument('email', type=str, required=True, help='email parameter is required')

    def get(self, user_id=None):
        if user_id:
            user = User.query.filter_by(id=user_id).first()
            return marshal(user, user_fields)
        else:
            args = request.args.to_dict()
            limit = args.get('limit', 0)
            offset = args.get('offset', 0)

            args.pop('limit', None)
            args.pop('offset', None)

            user = User.query.filter_by(**args).order_by(User.id)
            if limit:
                user = user.limit(limit)

            if offset:
                user = user.offset(offset)

            user = user.all()

            return marshal({
                'count': len(user),
                'users': [marshal(u, user_fields) for u in user]
            }, user_list_fields)

    @marshal_with(user_fields)
    def post(self):
        args = UserResource.user_post_parser.parse_args()
        user = User(**args)
        DB.session.add(user)
        DB.session.commit()

        return user

    @marshal_with(user_fields)
    def put(self, user_id=None):
        user = User.query.get(user_id)

        if 'name' in request.json:
            user.name = request.json['name']
        if 'email' in request.json:
            user.email = request.json['email']

        DB.session.commit()
        return user

    @marshal_with(user_fields)
    def delete(self, user_id=None):
        user = User.query.get(user_id)

        DB.session.delete(user)
        DB.session.commit()

        return user
