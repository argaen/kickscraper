from .backends.kickstarter.client import KickStarter
from .backends.kickstarter.models import KickStarterProject as Project


def search_project(terms):
    return KickStarter().search_project(terms)


def search_projects(terms):
    return KickStarter().search_projects(terms)
