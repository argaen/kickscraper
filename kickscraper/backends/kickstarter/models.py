from kickscraper.backends.kickstarter import client


class KickStarterProject:

    def __init__(self, name):
        self.name = name
        self.project_json = None
        self.load()

    def __getattr__(self, name):
        return self._get_data(name)

    def _get_data(self, key):
        if not self.project_json:
            self.load()
        return self.project_json[key]

    def load(self):
        self.project_json = client.KickStarter().search_project(self.name)
