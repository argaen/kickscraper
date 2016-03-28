# KickScraper

This project offers an API to consult Kickstarter projects information. It does that by scrapping the website or accesing undocumented APIs so this software is provided as it is.

To check everything is working correctly and the needed data is able to be pulled from the Kickstarter page, from the project root execute:

`PYTHONPATH=. py.test`

To install, just execute:

`pip install kickscraper`

# Usage

The normal usage flow with this package is to search for a project and then access its information. Some examples:

```python
>>> from kickscraper import Project
>>> p = Project(name='Exploding kittens')
>>> p.title
'Exploding Kittens'
>>> p.state
'successful'
>>> p.pledged
8782571.99
>>> p.goal
10000.0
>>> p.launched
1421776819
>>> p.deadline
1424397600
>>> p.backers_count
219382
>>> p.photo['thumb']
'https://ksr-ugc.imgix.net/projects/1542071/photo-original.png?v=1420836802&w=40&h=30&fit=crop&auto=format&q=92&s=13dfdfc7e3b916eba80e19fdea09ebd9'
>>> p.rewards
{'3531560': {'backers': '15,505 backers',
    'description': "THE EXPLODING KITTENS DECK\nOne copy of Exploding Kittens. (Ages 7+)\n-To order multiple decks, just add $20 for each extra deck you'd like. (extra shipping charges may apply)\n\nLess",
    'title': 'Pledge $20 or more\n\n\nAbout $20 USD',
    'uid': '3531560'},
'3531561': {'backers': '202,934 backers',
    'description': "THE NSFW DECK\nOne copy of the Exploding Kittens deck PLUS one copy of the NSFW deck.  This is a deck of bonus cards that were too horrible/incredible to include in the kid friendly version.   (Ages 30+)\n-To order multiple pairs of decks, just add $35 for each extra pair of decks you'd like. (extra shipping charges may apply)\n\nLess",
    'title': 'Pledge $35 or more\n\n\nAbout $35 USD',
    'uid': '3531561'},
'3531562': {'backers': '200 backers\n\nAll gone!',
    'description': "THE COLLECTOR'S DECK\nTwo copies of both decks from the previous reward but one of each will be signed by the creators of the game.  (So you don't have to ruin the fancy signed decks with your filthy game playing hands.)\n\nLess",
    'title': 'Pledge $100 or more\n\n\nAbout $100 USD',
    'uid': '3531562'},
'3571711': {'backers': '5 backers\n\nAll gone!',
    'description': "THE DECK OF LEGENDS\nEverything from the previous reward PLUS each of the game creators will draw you a custom card. (We apologize in advance for Elan's drawing skills.)\n\nLess",
    'title': 'Pledge $500 or more\n\n\nAbout $500 USD',
    'uid': '3571711'}}
>>> p.early_birds
{'3531562': {'backers_left': 0,
  'description': "THE COLLECTOR'S DECK\nTwo copies of both decks from the previous reward but one of each will be signed by the creators of the game.  (So you don't have to ruin the fancy signed decks with your filthy game playing hands.)\n\nLess",
  'title': 'Pledge $100 or more',
  'uid': '3531562'},
 '3571711': {'backers_left': 0,
  'description': "THE DECK OF LEGENDS\nEverything from the previous reward PLUS each of the game creators will draw you a custom card. (We apologize in advance for Elan's drawing skills.)\n\nLess",
  'title': 'Pledge $500 or more',
  'uid': '3571711'}}
```

For the KickStarter backend, there is a `project_json` attribute that allows to retrieve the extra information retrieved from the query to the HTTP endpoint. You can also access this attributs in a normal way with `p.connector.<attribute_name>`.

```python
>>> p.connector
<kickscraper.backends.kickstarter.models.KickStarterProject object at 0x7f2ace952b00>
>>> p.connector.project_json["creator"]
{'id': 1281334714, 'name': 'Elan Lee', 'slug': 'elanlee', 'urls': {'api': {'user': 'https://api.kickstarter.com/v1/users/1281334714?signature=1455539957.142a29e448e4410d7571985d81f89f7820387092'}, 'web': {'user': 'https://www.kickstarter.com/profile/elanlee'}}, 'avatar': {'small': 'https://ksr-ugc.imgix.net/avatars/195345/mmotel_elan_lee_05_on_white_0592-2.original.jpg?v=1419440819&w=80&h=80&fit=crop&auto=format&q=92&s=7a5f8ccef6aec840b071b227f0c8857f', 'medium': 'https://ksr-ugc.imgix.net/avatars/195345/mmotel_elan_lee_05_on_white_0592-2.original.jpg?v=1419440819&w=160&h=160&fit=crop&auto=format&q=92&s=b7f47cefe817c8e4d60e8fb6bc59312b', 'thumb': 'https://ksr-ugc.imgix.net/avatars/195345/mmotel_elan_lee_05_on_white_0592-2.original.jpg?v=1419440819&w=40&h=40&fit=crop&auto=format&q=92&s=fe45920ced0997320f5d5a60321fbde7'}}
>>> p.connector.creator
{'id': 1281334714, 'name': 'Elan Lee', 'slug': 'elanlee', 'urls': {'api': {'user': 'https://api.kickstarter.com/v1/users/1281334714?signature=1455539957.142a29e448e4410d7571985d81f89f7820387092'}, 'web': {'user': 'https://www.kickstarter.com/profile/elanlee'}}, 'avatar': {'small': 'https://ksr-ugc.imgix.net/avatars/195345/mmotel_elan_lee_05_on_white_0592-2.original.jpg?v=1419440819&w=80&h=80&fit=crop&auto=format&q=92&s=7a5f8ccef6aec840b071b227f0c8857f', 'medium': 'https://ksr-ugc.imgix.net/avatars/195345/mmotel_elan_lee_05_on_white_0592-2.original.jpg?v=1419440819&w=160&h=160&fit=crop&auto=format&q=92&s=b7f47cefe817c8e4d60e8fb6bc59312b', 'thumb': 'https://ksr-ugc.imgix.net/avatars/195345/mmotel_elan_lee_05_on_white_0592-2.original.jpg?v=1419440819&w=40&h=40&fit=crop&auto=format&q=92&s=fe45920ced0997320f5d5a60321fbde7'}}
```

There are also a couple endpoints that allow you to search for projects (`kickscraper.search_projects`) and fetch the first one from the returned list (`kickscraper.search_project`):

```python
>>> kickscraper.search_projects("Kittens")['total_hits']
116
>>> kickscraper.search_project("Kittens")["name"]
'Laser Kittens: an RPG about tiny kitties growing up'
>>> kickscraper.search_project("Explode Kittens")["name"]
'Exploding Kittens'
```

Internally, the `Project` class uses the `search_project` to fetch the project according to the given name. Be careful with this because you may be pulling the wrong project (i.e, for the _Kittens_ search I would expect to load the _Exploding Kittens_ first rather than _Laser Kittens_ project).

# Class Reference

## Project

- **Project.uid: int**
- **Project.title: str**
- **Project.photo: dict**
- **Project.pledged: float**
- **Project.goal: float**
- **Project.state: str**
- **Project.currency: str**
- **Project.launched: int (unix time)**
- **Project.deadline: int (unix time)**
- **Project.backers\_count: int**
- **Project.rewards: dict**
- **Project.early\_birds: dict**


# TODO

- Tests need to be more intelligent. Mb using parametrized pytest tests or so. Need to
  reuse the ones from main and from the backends or something...
- Add logs.
- Allow to load projects given a uid or url?.
- More intelligent way to load projects (check if search by popularity exists).
