"""This module includes views of movies app"""
from flask import Blueprint, render_template
from app.movies.helpers import collect_movies

movies = Blueprint('movies', __name__)


@movies.route('/movies', methods=['GET'])
def get_movies():
    """The /movies endpoint vies
    Returns:
        Template rendered with movies collected and
        fetch time
    """
    info = collect_movies()
    return render_template('movies.html',
                           movies=info['movies'],
                           fetched_at=info['fetched_at'])
