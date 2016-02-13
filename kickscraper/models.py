# TODO: Need to improve this to allow full paths in strings!
from kickscraper.backends.kickstarter import models
DEFAULT_BACKEND = 'KickStarterProject'


# TODO: Define a standard interface to access attributes from different backends,
# its okay to let access anything but need to provide a standard/unified one.
class Project:

    def __init__(self, name, backend=None):
        self.connector = getattr(models, DEFAULT_BACKEND)(name)

    def __getattr__(self, name):
        return getattr(self.connector, name)
