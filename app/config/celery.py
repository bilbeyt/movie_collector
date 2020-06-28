"""This module is settings for celery"""
from celery.schedules import crontab


CeleryConfig = {
    'BROKER_URL': 'redis://localhost:6379/0',
    'CELERY_IMPORTS': ['app.movies.tasks'],
    'RESULT_BACKEND': 'redis://localhost:6379/0',
    'CELERYBEAT_SCHEDULE': {
        'movie-collect': {
            'task': 'movie_collector',
            'schedule': crontab(minute='*'),
        }
    }
}
    