from .backends.kickstarter.client import KickStarter


def search_project(terms):
    return KickStarter().search_project(terms)


def search_projects(terms):
    return KickStarter().search_projects(terms)
