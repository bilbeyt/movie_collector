"""This module includes GhibliStudio related classes"""
import logging
import requests

from app.movies.adapters.base import BaseMovieProviderAdapter


logger = logging.getLogger(__name__)


class GhibliStudioAdapter(BaseMovieProviderAdapter):
    """This class is adapter for GhibliStudio"""
    @staticmethod
    def parse_movies(request_body):
        movies = {}
        for movie in request_body:
            movies[movie['url']] = {
                "title": movie['title'],
                "release_date": movie['release_date'],
                "people": []
            }
        return movies

    def __init__(self):
        self.base_url = "https://ghibliapi.herokuapp.com"

    def get_people(self):
        endpoint = f"{self.base_url}/people?fields=name,films"
        request = requests.get(endpoint)
        body = []
        if request.status_code == 200:
            body = request.json()
        return body

    def get_movies(self):
        endpoint = f"{self.base_url}/films?fields=title,url,release_date"
        request = requests.get(endpoint)
        body = []
        if request.status_code == 200:
            body = request.json()
        return body

    def collect(self):
        movies = self.get_movies()
        movies = self.parse_movies(movies)
        people = self.get_people()
        for person in people:
            for film in person['films']:
                movies[film]['people'].append(person['name'])
        movies = sorted(movies.items(),
                        key=lambda m: m[1]['release_date'],
                        reverse=True)
        return dict(movies)
