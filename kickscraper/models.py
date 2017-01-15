from .client import KickStarterClient


class Project:

    def __init__(self, name):
        self._search_by = name
        self.project_json = None
        self._rewards = None
        self._early_birds = None
        self._reload()

    @property
    def uid(self):
        return self._get_data('id')

    @property
    def name(self):
        return self._get_data('name')

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
    def launched_at(self):
        return self._get_data('launched_at')

    @property
    def deadline(self):
        return self._get_data('deadline')

    @property
    def backers_count(self):
        return self._get_data('backers_count')

    @property
    def rewards(self, force_reload=True):
        if not self._rewards or force_reload:
            self._rewards = KickStarterClient().get_rewards(self.creator["slug"], self.slug)
        return self._rewards

    @property
    def early_birds(self, force_reload=True):
        if not self._early_birds or force_reload:
            self._early_birds = KickStarterClient().get_early_birds(
                self.creator["slug"], self.slug)
        return self._early_birds

    def __getattr__(self, attr):
        return self._get_data(attr)

    def _get_data(self, key):
        if not self.project_json:
            self._reload()
        if key in self.project_json:
            return self.project_json[key]
        else:
            raise AttributeError("Project object has no attribute %s" % key)

    def _reload(self):
        self.project_json = KickStarterClient().search_project(self._search_by)
