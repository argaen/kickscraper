import os
import requests
import re
import bs4


class KickStarterClient:

    API_ROOT = "https://www.kickstarter.com/"
    PROJECTS = 'projects'
    STATS = 'stats.json'
    REWARDS = 'rewards'

    def get_project(self, creator, title):
        project_dict = {}
        response = requests.get(
            os.path.join(self.API_ROOT, self.PROJECTS, creator, title))
        if not response.ok:
            return {}
        soup = bs4.BeautifulSoup(response.content, "lxml")

        pre_title_div = soup.find("div", class_="col col-8 py2")
        title = pre_title_div.find("h3", class_="normal") if pre_title_div else ""

        project_dict["title"] = title.text.strip() if title else title.replace('-', ' ').title()
        project_dict["hours_to_go"] = soup.find("span", id="project_duration_data")["data-hours-remaining"] if soup.find("span", id="project_duration_data") else None
        project_dict["image"] = soup.find("div", class_="project-image").find("img")["src"] if soup.find("div", class_="project-image") else ""

        return project_dict

    def get_early_birds(self, creator, name):
        return self.get_json_early_birds(creator, name)

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
