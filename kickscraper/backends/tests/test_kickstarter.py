import pytest

from kickscraper.backends.kickstarter import client
from kickscraper.backends.kickstarter import models


@pytest.fixture
def k():
    return client.KickStarter()


@pytest.fixture
def p():
    return models.KickStarterProject(uid=1946925378, name="Mamma Coal-Reimagining Willie Nelson's Outlaw Concept Album")


class TestKickStarterClient:

    def test_get_stats(self, k):
        uid = 'carrastasney/mamma-coal-reimagining-willie-nelsons-outlaw-conce'
        keys = ['pledged', 'backers_count']
        d = k._get_project_stats(uid)
        assert d['project']['id'] == 1946925378
        for k in keys:
            assert k in d['project']

    def test_get_projects(self, k):
        terms = "mamma coal"
        keys = ['total_hits', 'projects']
        subkeys = ['id', 'photo', 'name', 'goal', 'pledged', 'state', 'deadline', 'launched_at', 'backers_count', 'usd_pledged', 'creator']
        d = k.search_projects(terms)
        for k in keys:
            assert k in d
        for k in subkeys:
            assert k in d['projects'][0]


class TestKickStarterModel:

    def test_create(self):
        subkeys = ['id', 'photo', 'name', 'goal', 'pledged', 'state', 'deadline', 'launched_at', 'backers_count', 'usd_pledged', 'creator']
        p = models.KickStarterProject(uid=1946925378, name="Mamma Coal-Reimagining Willie Nelson's Outlaw Concept Album")
        p.reload()
        assert p.project_json is not None
        for k in subkeys:
            assert k in p.project_json

    def test_get_goal(self, p):
        assert type(p.goal) == float

    def test_get_author(self, p):
        assert type(p.author) == str

    def test_get_pledged(self, p):
        assert type(p.pledged) == str

    def test_get_time_to_go(self, p):
        assert type(p.time_to_go) == int
