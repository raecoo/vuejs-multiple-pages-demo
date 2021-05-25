from flask import Blueprint

website_bp = Blueprint('website_endpoint', __name__)

from server.website import routes
