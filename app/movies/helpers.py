"""This module includes helper functions for movies app"""
from datetime import datetime
from app import cache
from app.movies.adapters.ghibli import GhibliStudioAdapter


def collect_movies():
    """This function collects movies and
    set cache if cache is empty
    Returns:
        A dict mapping movies collected and
        stores fetch time
    """
    info = cache.get('movies_info')
    if info is None:
        movie_client = GhibliStudioAdapter()
        movies = movie_client.collect()
        fetched_at = datetime.now().isoformat()
        info = {
            'fetched_at': fetched_at,
            'movies': movies
        }
        cache.set('movies_info', info, timeout=60)
    return info
