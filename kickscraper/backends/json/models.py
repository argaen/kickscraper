import os
import json

from kickscraper.backends.models import BaseProject


class JsonProject(BaseProject):

    def __init__(self, json_file):
        basepath = os.path.dirname(os.path.realpath(__file__))
        with open(os.path.join(basepath, '../fixtures', json_file), 'r') as f:
            self.project_json = json.load(f)
            self._rewards = None
            self._early_birds = None

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
        return self._rewards

    @property
    def early_birds(self, force_reload=True):
        return self._early_birds

    def __getattr__(self, name):
        return self._get_data(name)

    def _get_data(self, key):
        if key in self.project_json:
            return self.project_json[key]
        else:
            raise AttributeError("JsonProject object has no attribute %s" % key)
