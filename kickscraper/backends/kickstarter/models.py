from kickscraper.backends.models import BaseProject
from kickscraper.backends.kickstarter import client


class KickStarterProject(BaseProject):

    attributes_mapping = {
        'uid': 'id',
        'title': 'name',
        'launched': 'launched_at',
    }

    def __init__(self, name):
        self.name = name
        self.project_json = None
        self._rewards = None
        self._early_birds = None
        self._reload()

    @property
    def uid(self):
        return self._get_data('uid')

    @property
    def title(self):
        return self._get_data('title')

    @property
    def photo(self):
        return self._get_data('photo')

    @property
    def pledged(self):
        return self._get_data('pledged')

    @property
    def goal(self):
        return self._get_data('goal')

    @property
    def state(self):
        return self._get_data('state')

    @property
    def currency(self):
        return self._get_data('currency')

    @property
    def launched(self):
        return self._get_data('launched')

    @property
    def deadline(self):
        return self._get_data('deadline')

    @property
    def backers_count(self):
        return self._get_data('backers_count')

    @property
    def rewards(self, force_reload=True):
        if not self._rewards or force_reload:
            self._rewards = client.KickStarter().get_rewards(self.creator["slug"], self.slug)
        return self._rewards

    @property
    def early_birds(self, force_reload=True):
        if not self._early_birds or force_reload:
            self._early_birds = client.KickStarter().get_early_birds(self.creator["slug"], self.slug)
        return self._early_birds

    def __getattr__(self, name):
        return self._get_data(name)

    def _get_data(self, key):
        if not self.project_json:
            self._reload()
        key = self.attributes_mapping.get(key) or key
        if key in self.project_json:
            return self.project_json[self.attributes_mapping.get(key) or key]
        else:
            raise AttributeError("KickStarter object has no attribute %s" % key)

    def _reload(self):
        self.project_json = client.KickStarter().search_project(self.name)
