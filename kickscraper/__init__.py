from .models import Project
from .client import KickStarterClient


__all__ = (
    'Project',
    'search_project',
    'search_projects'
)


def search_project(terms):
    return KickStarterClient().search_project(terms)


def search_projects(terms):
    return KickStarterClient().search_projects(terms)
