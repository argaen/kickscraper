# TODO: Define a standard interface to access attributes from different backends,
# its okay to let access anything but need to provide a standard/unified one.
from .backends.kickstarter import models

DEFAULT_BACKEND = 'KickStarterProject'


class Project:

    def __init__(self, name, backend=None):
        self.connector = getattr(models, DEFAULT_BACKEND)(name)

    @property
    def rewards(self):
        return self.connector.rewards

    @property
    def early_birds(self):
        return self.connector.early_birds

    def __getattr__(self, name):
        return getattr(self.connector, name)
