# TODO: Define a standard interface to access attributes from different backends,
# its okay to let access anything but need to provide a standard/unified one.
from .backends.kickstarter import models

DEFAULT_BACKEND = 'KickStarterProject'


class Project:

    ATTRIBUTES = [
        'uid', 'title', 'photo', 'pledged', 'goal', 'state', 'currency',
        'launched', 'deadline', 'backers_count']

    def __init__(self, name, backend=None):
        self.connector = getattr(models, DEFAULT_BACKEND)(name)

    @property
    def rewards(self):
        return self.connector.get_rewards()

    @property
    def early_birds(self):
        return self.connector.get_early_birds()

    def __getattr__(self, name):
        if name in self.ATTRIBUTES:
            return getattr(self.connector, name)
        raise AttributeError
