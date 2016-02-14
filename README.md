# KickScraper

This project offers an API to consult Kickstarter projects information. It does that by scrapping the website or accesing undocumented APIs so this software is provided as it is. No guarantee is assured.

To check everything is working correctly and the needed data is able to be pulled from the Kickstarter page, from the project root execute:

`PYTHONPATH=. py.test`

# Usage

The normal usage flow with this package is to search for a project and then access its information. Some examples:

```python
>>> from kickscraper.models import Project
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
>>> Project(name="Zombicide Plague").title
'Zombicide: Black Plague'
>>> p.connector
<kickscraper.backends.kickstarter.models.KickStarterProject object at 0x7f2ace952b00>
>>> p.connector.project_json["creator"]
{'id': 1281334714, 'name': 'Elan Lee', 'slug': 'elanlee', 'urls': {'api': {'user': 'https://api.kickstarter.com/v1/users/1281334714?signature=1455539957.142a29e448e4410d7571985d81f89f7820387092'}, 'web': {'user': 'https://www.kickstarter.com/profile/elanlee'}}, 'avatar': {'small': 'https://ksr-ugc.imgix.net/avatars/195345/mmotel_elan_lee_05_on_white_0592-2.original.jpg?v=1419440819&w=80&h=80&fit=crop&auto=format&q=92&s=7a5f8ccef6aec840b071b227f0c8857f', 'medium': 'https://ksr-ugc.imgix.net/avatars/195345/mmotel_elan_lee_05_on_white_0592-2.original.jpg?v=1419440819&w=160&h=160&fit=crop&auto=format&q=92&s=b7f47cefe817c8e4d60e8fb6bc59312b', 'thumb': 'https://ksr-ugc.imgix.net/avatars/195345/mmotel_elan_lee_05_on_white_0592-2.original.jpg?v=1419440819&w=40&h=40&fit=crop&auto=format&q=92&s=fe45920ced0997320f5d5a60321fbde7'}}
>>> p.connector.creator
{'id': 1281334714, 'name': 'Elan Lee', 'slug': 'elanlee', 'urls': {'api': {'user': 'https://api.kickstarter.com/v1/users/1281334714?signature=1455539957.142a29e448e4410d7571985d81f89f7820387092'}, 'web': {'user': 'https://www.kickstarter.com/profile/elanlee'}}, 'avatar': {'small': 'https://ksr-ugc.imgix.net/avatars/195345/mmotel_elan_lee_05_on_white_0592-2.original.jpg?v=1419440819&w=80&h=80&fit=crop&auto=format&q=92&s=7a5f8ccef6aec840b071b227f0c8857f', 'medium': 'https://ksr-ugc.imgix.net/avatars/195345/mmotel_elan_lee_05_on_white_0592-2.original.jpg?v=1419440819&w=160&h=160&fit=crop&auto=format&q=92&s=b7f47cefe817c8e4d60e8fb6bc59312b', 'thumb': 'https://ksr-ugc.imgix.net/avatars/195345/mmotel_elan_lee_05_on_white_0592-2.original.jpg?v=1419440819&w=40&h=40&fit=crop&auto=format&q=92&s=fe45920ced0997320f5d5a60321fbde7'}}
```

For the KickStarter backend, there is a `project_json` attribute that allows to retrieve the extra information retrieved from the query to the HTTP endpoint. You can also access this attributs in a normal way with `p.connector.<attribute_name>`.

There are also a couple endpoints that allow you to search for projects (`search_projects`) and fetch the first one from the returned list (`search_project`):

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


# TODO

- Rewards query.
- Tests need to be more intelligent. Mb using parametrized pytest tests or so. Need to
  reuse the ones from main and from the backends or something...
- Add logs.
- Allow to load projects given a uid or url?.
- More intelligent way to load projects (check if search by popularity exists).
- Allow dynamic and multiple backends for the Project class.
