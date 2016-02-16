import os
import requests
import bs4

API_ROOT = "https://www.kickstarter.com/"
PROJECTS_URL = 'projects'
REWARDS_URL = 'rewards'


def get_json_rewards(creator, name):
    rewards_dict = {}
    rewards = _get_rewards_divs(creator, name)
    for hr in rewards:
        r = _html_reward_to_json(hr)
        rewards_dict[r['uid']] = r

    return rewards_dict


def _get_rewards_divs(creator, name):
    r = requests.get(os.path.join(API_ROOT, PROJECTS_URL, creator, name, REWARDS_URL))
    soup = bs4.BeautifulSoup(r._content, "html.parser")
    return soup.find_all("li", class_="pledge-selectable-sidebar")


def _html_reward_to_json(reward):
    uid = reward['data-reward-id']

    pledge_info = reward.find("div", class_="pledge__info")
    title = pledge_info.find("h2", class_="pledge__amount").text.strip('\n ')
    backers = pledge_info.find("p", class_="pledge__backer-count").text.strip('\n ')
    description = pledge_info.find("div", class_="pledge__reward-description").text.strip('\n ')

    return {
        'uid': uid,
        'title': title,
        'backers': backers,
        'description': description,
    }
