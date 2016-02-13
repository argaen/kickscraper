# TODO: Need to improve this to allow full paths in strings!
from kickscraper.backends.kickstarter import models
DEFAULT_BACKEND = 'KickStarterProject'


class Project:

    def __init__(self, uid, name, backend=None):
        self.connector = getattr(models, DEFAULT_BACKEND)(uid, name)

    @property
    def title(self):
        return self.connector.title

    @property
    def time_to_go(self):
        return self.connector.time_to_go

    def get_author():
        pass
