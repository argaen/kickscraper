# TODO: Need to improve this to allow full paths in strings!
from .backends.kickstarter.client import KickStarter
from .models import Project


def search_project(terms):
    return KickStarter().search_project(terms)


def search_projects(terms):
    return KickStarter().search_projects(terms)
