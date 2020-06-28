"""This module includes base classes for movie providers"""
from abc import ABC


class BaseMovieProviderAdapter(ABC):
    """Base movie provider adapter"""
    @staticmethod
    def parse_movies(request_body):
        """This method parses movies and
        people to create requested structure"""

    def get_people(self):
        """This method gets people from movie provider"""

    def get_movies(self):
        """This method gets movies from movie provider"""

    def collect(self):
        """This method collects movies"""
