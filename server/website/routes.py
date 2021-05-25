from flask import render_template

from server.website import website_bp


@website_bp.route('/')
@website_bp.route('/index')
def index():
    return render_template('index.html')


@website_bp.route('/ping')
def ping():
    return render_template('ping.html')
