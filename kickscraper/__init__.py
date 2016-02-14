# TODO: Need to improve this to allow full paths in strings!
from kickscraper.backends.kickstarter.client import KickStarter
DEFAULT_BACKEND = 'KickStarterProject'


def search_project(terms):
    return KickStarter().search_project(terms)


def search_projects(terms):
    print(KickStarter().search_projects(terms))
    return KickStarter().search_projects(terms)
