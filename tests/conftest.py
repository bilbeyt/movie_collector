"""Pytest configuration module"""
import pytest
from app import cache as app_cache
from app.celery import celery
from app.movies.views import app as application

@pytest.fixture
def app():
    """Test application initalizer"""
    application.config.update({'TESTING': True})
    return application

@pytest.fixture
def client(app):
    """Test application client initalizer"""
    with app.test_client() as test_client:
        yield test_client

@pytest.fixture
def cache():
    """Test application cache initalizer"""
    app_cache.app.config.update({
        'CACHE_REDIS_DB': '1'
    })
    test_cache = app_cache
    test_cache.delete('movies_info')
    return app_cache

@pytest.fixture
def celery_app():
    """Test celery application initalizer"""
    celery.conf.update({
        'BROKER_URL': 'redis://localhost:6379/1',
        'RESULT_BACKEND': 'redis://localhost:6379/1',
        'CELERY_RESULT_BACKEND': 'redis://localhost:6379/1'
    })
    return celery

@pytest.fixture
def celery_worker_parameters():
    """Test celery worker without ping job"""
    return {
        'perform_ping_check': False
    }
