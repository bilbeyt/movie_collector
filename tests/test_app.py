"""Application based tests"""
from app.movies.tasks import get_movies
from app.movies.helpers import collect_movies


def test_movies_task_cache_empty(celery_app, celery_worker, cache):
    """Tests for checking if cache is not empty after celery task"""
    get_movies.delay().get(timeout=10)
    assert cache.get('movies_info') is not None

def test_collect_movies_use_cache(cache):
    """Tests for checking if cache is used if exists"""
    run_info = collect_movies() # fill the cache
    cache_info = collect_movies() # got from cache
    assert run_info['fetched_at'] == cache_info['fetched_at']

def test_check_movies_endpoint(client):
    """Tests for checking if movies endpoint returns 200"""
    response = client.get('/movies')
    assert response.status_code == 200
