from flask_restful import Api
from endpoints import APP


api = Api(APP)
api.prefix = '/api/v1'


from endpoints.routers.users.view import UserResource
from endpoints.routers import Home

## Blueprint of APP ##
api.add_resource(Home, '/')
api.add_resource(UserResource, '/users', '/users/<int:user_id>')


if __name__ == '__main__':
    APP.run()
