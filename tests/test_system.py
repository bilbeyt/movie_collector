"""System based tests for application"""
from app import create_app


def test_app_config(app):
    """Tests application configuration"""
    assert not create_app().testing
    assert app.testing

def test_cache_empty(cache):
    """Tests cache configuration"""
    assert cache.get('movies_info') is None
