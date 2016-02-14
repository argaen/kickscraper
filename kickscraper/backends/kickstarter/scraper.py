import requests
import bs4

URL = "https://www.kickstarter.com/projects/elanlee/exploding-kittens/rewards"


def get_json_rewards(name, creator):
    rewards_dict = {}
    rewards = _get_rewards_divs("hi", "ho")
    for r in rewards:
        k, e = _html_reward_to_json(r)
        rewards_dict[k] = e

    return rewards_dict


def _get_rewards_divs(name, creator):
    r = requests.get(URL)
    soup = bs4.BeautifulSoup(r._content, "html.parser")
    return soup.find_all("li", class_="pledge-selectable-sidebar")


def _html_reward_to_json(reward):
    uid = reward['data-reward-id']

    pledge_info = reward.find("div", class_="pledge__info")
    title = pledge_info.find("h2", class_="pledge__amount").text.strip('\n ')
    backers = pledge_info.find("p", class_="pledge__backer-count").text.strip('\n ')
    description = pledge_info.find("div", class_="pledge__reward-description").text.strip('\n ')

    return uid, (title, backers, description)
