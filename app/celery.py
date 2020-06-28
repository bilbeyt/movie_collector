"""This module is used to run celery worker"""

from celery import Celery
from flask_socketio import SocketIO
from app import app
from app.config.socket import SocketConfig


def make_celery(application):
    """This function creates Celery instance
    Args:
        app: Flask Application
    Returns:
        New Celery instance
    """
    celery_app = Celery(application.import_name)
    celery_app.conf.update(application.config)
    return celery_app


celery = make_celery(app)
socketio = SocketIO(**SocketConfig)
