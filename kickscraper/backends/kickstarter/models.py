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
        self._rewards = None
        self.load()

    def load(self):
        self.project_json = client.KickStarter().search_project(self.name)

    def get_rewards(self, force_reload=True):
        if not self._rewards or force_reload:
            self._rewards = client.KickStarter().get_rewards(self.creator["slug"], self.slug)
        return self._rewards

    def get_early_birds(self, force_reload=True):
        if not self._rewards or force_reload:
            self._rewards = client.KickStarter().get_rewards(self.creator["slug"], self.slug)
        return self._rewards

    def __getattr__(self, name):
        return self._get_data(name)

    def _get_data(self, key):
        if not self.project_json:
            self.load()
        return self.project_json.get(self.attributes_mapping.get(key) or key)
