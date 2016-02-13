from kickscraper.backends.kickstarter import client


class KickStarterProject:

    def __init__(self, uid, name):
        self.uid = uid
        self.name = name
        self.project_json = None

    @property
    def goal(self):
        return self._get_data('goal')

    @property
    def author(self):
        return self._get_data('creator')['name']

    @property
    def pledged(self):
        return self._get_data('pledged')

    @property
    def time_to_go(self):
        return self._get_data('time_to_go')

    def _get_data(self, key):
        if not self.project_json:
            self.reload()
        return self.project_json[key]

    def reload(self):
        self.project_json = client.KickStarter().search_project(self.name)
