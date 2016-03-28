import importlib

DEFAULT_BACKEND = 'kickscraper.backends.kickstarter.models.KickStarterProject'


class Project:

    def __init__(self, name, backend=DEFAULT_BACKEND):
        self.name = name
        module_name, class_name = backend.rsplit(".", 1)
        self.connector = getattr(importlib.import_module(module_name), class_name)(name)

    @property
    def rewards(self):
        return self.connector.rewards

    @property
    def early_birds(self):
        return self.connector.early_birds

    def __getattr__(self, name):
        return getattr(self.connector, name)
