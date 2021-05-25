from flask_restplus import Resource
from . import api_rest


@api_rest.route('/landing')
class Landing(Resource):
    def get(self):
        return {'code': 200}
