"""This module includes necessary function to create app"""

from flask import Flask
from flask_caching import Cache
from app.config.app import Config
from app.config.cache import CacheConfig
from app.config.celery import CeleryConfig


def create_app():
    '''This function creates Flask Application
    Returns:
        A new Flask Application
    '''
    application = Flask(__name__)
    application.config.update(Config)
    application.config.update(CacheConfig)
    application.config.update(CeleryConfig)
    return application


app = create_app()
cache = Cache(app)
