import os
import requests

API_ROOT = "https://www.kickstarter.com/"
PROJECTS_URL = 'projects'


class KickStarter:

    def search_projects(self, terms):
        url = os.path.join(API_ROOT, PROJECTS_URL, 'search.json?term=' + terms.replace(' ', '+'))
        r = requests.get(url)
        return r.json()

    def search_project(self, terms):
        return self.search_projects(terms)['projects'][0]

    def get_rewards(self, name, creator):
        print(name, creator)

    def _get_project_stats(self, uid):
        url = os.path.join(API_ROOT, PROJECTS_URL, uid, 'stats.json')
        r = requests.get(url)
        return r.json()
