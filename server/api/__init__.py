from flask import Blueprint
from flask_restplus import Api

website_bp = Blueprint('api_endpoint', __name__)

api_bp = Blueprint('api_endpoint', __name__, url_prefix='/api')

api_rest = Api(api_bp)
from server.api.landing import *


@api_bp.after_request
def add_header(response):
    response.headers[
        'Access-Control-Allow-Headers'] = 'Content-Type,Authorization'
    return response
