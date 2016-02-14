# TODO: Define a standard interface to access attributes from different backends,
# its okay to let access anything but need to provide a standard/unified one.
from kickscraper import DEFAULT_BACKEND
from kickscraper.backends.kickstarter import models


class Project:

    ATTRIBUTES = [
        'uid', 'title', 'photo', 'pledged', 'goal', 'state', 'currency',
        'launched', 'deadline', 'backers_count']

    def __init__(self, name, backend=None):
        self.connector = getattr(models, DEFAULT_BACKEND)(name)

    def __getattr__(self, name):
        if name in self.ATTRIBUTES:
            return getattr(self.connector, name)
        raise AttributeError
