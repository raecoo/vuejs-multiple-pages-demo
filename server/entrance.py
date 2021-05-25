from flask import Flask
from server.config import Config


def create_app(config_class=Config):
    class CustomFlask(Flask):
        jinja_options = Flask.jinja_options.copy()
        jinja_options.update(
            dict(
                block_start_string='(%',
                block_end_string='%)',
                variable_start_string='((',
                variable_end_string='))',
                comment_start_string='(#',
                comment_end_string='#)',
            ))

    app = CustomFlask(__name__,
                      static_url_path='/',
                      static_folder=config_class.DIST_DIR,
                      template_folder=config_class.DIST_DIR)

    app.config.from_object(config_class)

    from server.api import api_bp
    from server.website import website_bp

    app.register_blueprint(api_bp)
    app.register_blueprint(website_bp)

    print(config_class.APP_DIR, config_class.DIST_DIR, config_class.ROOT_DIR)
    return app


app = create_app()
