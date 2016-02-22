import os
import re
import requests
import bs4

API_ROOT = "https://www.kickstarter.com/"
PROJECTS_URL = 'projects'
REWARDS_URL = 'rewards'


def get_json_rewards(creator, name):
    rewards_dict = {}
    rewards = _get_rewards_divs(creator, name)
    for hr in rewards:
        r = _html_reward_to_json_reward(hr)
        rewards_dict[r['uid']] = r

    return rewards_dict


def _get_rewards_divs(creator, name):
    r = requests.get(os.path.join(API_ROOT, PROJECTS_URL, creator, name, REWARDS_URL))
    soup = bs4.BeautifulSoup(r._content, "html.parser")
    return soup.find_all("li", class_="pledge-selectable-sidebar")


def _html_reward_to_json_reward(reward):
    uid = reward['data-reward-id']

    pledge_info = reward.find("div", class_="pledge__info")
    title = pledge_info.find("h2", class_="pledge__amount").contents[0].strip('\n ')
    backers = pledge_info.find("p", class_="pledge__backer-count").text.strip('\n ')
    description = pledge_info.find("div", class_="pledge__reward-description").text.strip('\n ')

    return {
        'uid': uid,
        'title': title,
        'backers': backers,
        'description': description,
    }


def get_json_early_birds(creator, name):
    early_birds_dict = {}
    early_birds = _get_early_birds_divs(creator, name)
    for hr in early_birds:
        eb = _html_reward_to_json_early_bird(hr)
        early_birds_dict[eb['uid']] = eb

    return early_birds_dict


def _get_early_birds_divs(creator, name):
    reward_divs = _get_rewards_divs(creator, name)
    early_birds = [r for r in reward_divs if "pledge--all-gone" in r.get("class") or r.find("span", class_="pledge__limit")]
    return early_birds


def _html_reward_to_json_early_bird(reward):
    uid = reward['data-reward-id']

    pledge_info = reward.find("div", class_="pledge__info")

    title = pledge_info.find("h2", class_="pledge__amount").contents[0].strip('\n ')

    backers = pledge_info.find("p", class_="pledge__backer-count").text.strip('\n ')
    m = re.search("\((?P<left>[0-9]+) left of ([0-9]+)\)", backers)

    description = pledge_info.find("div", class_="pledge__reward-description").text.strip('\n ')

    return {
        'uid': uid,
        'title': title,
        'backers_left': int(m.group('left') if m else 0),
        'description': description,
    }
