"""This module includes the celery tasks for movies app"""
import logging
from app.celery import celery, socketio
from app.movies.helpers import collect_movies
from app import cache


logger = logging.getLogger(__name__)

@celery.task(name='movie_collector')
def get_movies():
    """This function is collecting movies and refreshes cache"""
    logger.info('Movie update task started!')
    cache.delete('movies_info')
    info = collect_movies()
    socketio.emit('update_movies', info,
                  namespace='/movies/stream')
    logger.info('Movies updated!')
