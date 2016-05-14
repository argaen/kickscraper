import pytest

from kickscraper.backends.kickstarter import client
from kickscraper.backends.kickstarter import models


@pytest.fixture
def k():
    return client.KickStarter()


@pytest.fixture
def p():
    return models.KickStarterProject(name="Mamma Coal-Reimagining Willie Nelson's Outlaw Concept Album")


@pytest.mark.kickstarter
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
        subkeys = ['id', 'photo', 'name', 'goal', 'pledged', 'state', 'deadline', 'launched_at', 'backers_count', 'usd_pledged', 'creator', 'currency_symbol', 'launched_at']
        d = k.search_projects(terms)
        for k in keys:
            assert k in d
        for k in subkeys:
            assert k in d['projects'][0]

    def test_get_rewards(self, k):
        rewards = k.get_rewards("elanlee", "exploding-kittens")
        assert len(rewards) == 4

    @pytest.mark.parametrize("creator, project, expected, available, all_gone", [
        ("elanlee", "exploding-kittens", 2, 0, 2),
        ("carrastasney", "mamma-coal-reimagining-willie-nelsons-outlaw-conce", 7, 7, 0),
    ])
    def test_get_early_birds(self, k, creator, project, expected, available, all_gone):
        early_birds = k.get_early_birds(creator, project)
        assert len(early_birds) == expected
        assert len([x for x, v in early_birds.items() if v["backers_left"] > 0]) == available
        assert len([x for x, v in early_birds.items() if v["backers_left"] == 0]) == all_gone


@pytest.mark.kickstarter
class TestKickStarterModel:

    def test_create(self):
        subkeys = ['id', 'photo', 'name', 'goal', 'pledged', 'state', 'deadline', 'launched_at', 'backers_count', 'usd_pledged', 'creator', 'currency_symbol', 'launched_at']
        p = models.KickStarterProject(name="Mamma Coal-Reimagining Willie Nelson's Outlaw Concept Album")
        p._reload()
        assert p.project_json is not None
        for k in subkeys:
            assert k in p.project_json

    def test_get_uid(self, p):
        assert type(p.uid) == int

    def test_get_title(self, p):
        assert type(p.title) == str

    def test_get_photo(self, p):
        assert type(p.photo) == dict

    def test_get_pledged(self, p):
        assert type(p.pledged) == float

    def test_get_goal(self, p):
        assert type(p.goal) == float

    def test_get_state(self, p):
        assert type(p.state) == str

    def test_get_currency(self, p):
        assert type(p.currency) == str

    def test_get_launched(self, p):
        assert type(p.launched) == int

    def test_get_deadline(self, p):
        assert type(p.deadline) == int

    def test_get_backers_count(self, p):
        assert type(p.backers_count) == int
