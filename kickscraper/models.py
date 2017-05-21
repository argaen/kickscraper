from .client import KickStarterClient


class Project:

    def __init__(self, uid):
        self.creator, self.title = uid.split('/')
        self._client = KickStarterClient()
        self.project_json = {}

    @property
    def hours_to_go(self):
        return self._get_data('hours_to_go')

    @property
    def image(self):
        return self._get_data('image')

    @property
    def early_birds(self, force_reload=True):
        return self._client.get_early_birds(self.creator, self.title)

    def _get_data(self, key):
        if key in self.project_json:
            return self.project_json[key]
        else:
            raise AttributeError("Project object has no attribute %s" % key)

    def load(self):
        self.project_json = self._client.get_project(self.creator, self.title)
