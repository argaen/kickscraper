from kickscraper.backends.kickstarter import client


class KickStarterProject:

    attributes_mapping = {
        'uid': 'id',
        'title': 'name',
        'launched': 'launched_at',
    }

    def __init__(self, name):
        self.name = name
        self.project_json = None
        self.load()

    def __getattr__(self, name):
        return self._get_data(name)

    def _get_data(self, key):
        if not self.project_json:
            self.load()
        return self.project_json.get(self.attributes_mapping.get(key) or key)

    def load(self):
        self.project_json = client.KickStarter().search_project(self.name)
