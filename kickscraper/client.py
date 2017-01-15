import os
import requests
import re
import bs4


class KickStarterClient:

    API_ROOT = "https://www.kickstarter.com/"
    PROJECTS_URL = 'projects'
    REWARDS_URL = 'rewards'

    def search_projects(self, terms):
        url = os.path.join(
            self.API_ROOT, self.PROJECTS_URL, 'search.json?term=' + terms.replace(' ', '+'))
        r = requests.get(url)
        return r.json()

    def search_project(self, terms):
        return self.search_projects(terms)['projects'][0]

    def get_rewards(self, creator, name):
        return self.get_json_rewards(creator, name)

    def get_early_birds(self, creator, name):
        return self.get_json_early_birds(creator, name)

    def _get_project_stats(self, uid):
        url = os.path.join(self.API_ROOT, self.PROJECTS_URL, uid, 'stats.json')
        r = requests.get(url)
        return r.json()

    def get_json_rewards(self, creator, name):
        rewards_dict = {}
        rewards = self._get_rewards_divs(creator, name)
        for hr in rewards:
            r = self._html_reward_to_json_reward(hr)
            rewards_dict[r['uid']] = r

        return rewards_dict

    def _get_rewards_divs(self, creator, name):
        r = requests.get(
            os.path.join(self.API_ROOT, self.PROJECTS_URL, creator, name, self.REWARDS_URL))
        soup = bs4.BeautifulSoup(r._content, "html.parser")
        return soup.find_all("li", class_="pledge-selectable-sidebar")

    def _html_reward_to_json_reward(self, reward):
        uid = reward['data-reward-id']

        pledge_info = reward.find("div", class_="pledge__info")
        title = pledge_info.find("h2", class_="pledge__amount").text.split('\n')[1]
        backers = pledge_info.find("span", class_="pledge__backer-count").text.strip('\n ')
        description = pledge_info.find("div", class_="pledge__reward-description").text.strip('\n ')

        return {
            'uid': uid,
            'title': title,
            'backers': backers,
            'description': description,
        }

    def get_json_early_birds(self, creator, name):
        early_birds_dict = {}
        early_birds = self._get_early_birds_divs(creator, name)
        for hr in early_birds:
            eb = self._html_reward_to_json_early_bird(hr)
            early_birds_dict[eb['uid']] = eb

        return early_birds_dict

    def _get_early_birds_divs(self, creator, name):
        reward_divs = self._get_rewards_divs(creator, name)
        early_birds = [
            r for r in reward_divs if
            "pledge--all-gone" in r.get("class") or r.find("span", class_="pledge__limit")
        ]
        return early_birds

    def _html_reward_to_json_early_bird(self, reward):
        uid = reward['data-reward-id']

        pledge_info = reward.find("div", class_="pledge__info")
        title = pledge_info.find("h2", class_="pledge__amount").text.split('\n')[1]
        backers = pledge_info.find("div", class_="pledge__backer-stats").text.strip('\n ')
        m = re.search("\((?P<left>[0-9]+) left of ([0-9]+)\)", backers)
        description = pledge_info.find("div", class_="pledge__reward-description").text.strip('\n ')

        return {
            'uid': uid,
            'title': title,
            'backers_left': int(m.group('left') if m else 0),
            'description': description,
        }
