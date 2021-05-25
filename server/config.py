"""
Global Flask Application Setting

See `.flaskenv` for default settings.
 """

import os


class Config(object):
    APP_DIR = os.path.dirname(__file__)
    ROOT_DIR = os.path.dirname(APP_DIR)
    DIST_DIR = os.path.join(ROOT_DIR, 'dist')
    STATIC_DIR = os.path.join(ROOT_DIR, 'static')

    if not os.path.exists(DIST_DIR):
        raise Exception('DIST_DIR not found: {}'.format(DIST_DIR))
