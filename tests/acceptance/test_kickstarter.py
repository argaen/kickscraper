import pytest

from kickscraper import KickStarterClient
from kickscraper import Project


@pytest.fixture
def client():
    return KickStarterClient()


@pytest.fixture
def project():
    return Project(name="Mamma Coal-Reimagining Willie Nelson's Outlaw Concept Album")


class TestClient:

    def test_get_stats(self, client):
        uid = 'carrastasney/mamma-coal-reimagining-willie-nelsons-outlaw-conce'
        keys = ['pledged', 'backers_count']
        d = client._get_project_stats(uid)
        assert d['project']['id'] == 1946925378
        for k in keys:
            assert k in d['project']

    def test_get_projects(self, client):
        terms = "mamma coal"
        keys = ['total_hits', 'projects']
        subkeys = [
            'id', 'photo', 'name', 'goal', 'pledged', 'state', 'deadline', 'launched_at',
            'backers_count', 'usd_pledged', 'creator', 'currency_symbol', 'launched_at']
        d = client.search_projects(terms)
        for k in keys:
            assert k in d
        for k in subkeys:
            assert k in d['projects'][0]

    def test_get_rewards(self, client):
        rewards = client.get_rewards("elanlee", "exploding-kittens")
        assert len(rewards) == 4

    @pytest.mark.parametrize("creator, project, expected, available, all_gone", [
        ("elanlee", "exploding-kittens", 2, 0, 2),
        ("1902165813", "ayo-the-clown-inspired-by-super-mario", 12, 0, 12),
    ])
    def test_get_early_birds(self, client, creator, project, expected, available, all_gone):
        early_birds = client.get_early_birds(creator, project)
        assert len(early_birds) == expected
        assert len([x for x, v in early_birds.items() if v["backers_left"] > 0]) == available
        assert len([x for x, v in early_birds.items() if v["backers_left"] == 0]) == all_gone


class TestProject:

    def test_create(self):
        subkeys = [
            'id', 'photo', 'name', 'goal', 'pledged', 'state', 'deadline', 'launched_at',
            'backers_count', 'usd_pledged', 'creator', 'currency_symbol', 'launched_at']
        p = Project(name="Mamma Coal-Reimagining Willie Nelson's Outlaw Concept Album")
        p._reload()
        assert p.project_json is not None
        for k in subkeys:
            assert k in p.project_json

    def test_get_uid(self, project):
        assert type(project.uid) == int

    def test_get_name(self, project):
        assert type(project.name) == str

    def test_get_photo(self, project):
        assert type(project.photo) == dict

    def test_get_pledged(self, project):
        assert type(project.pledged) == float

    def test_get_goal(self, project):
        assert type(project.goal) == float

    def test_get_state(self, project):
        assert type(project.state) == str

    def test_get_currency(self, project):
        assert type(project.currency) == str

    def test_get_launched(self, project):
        assert type(project.launched_at) == int

    def test_get_deadline(self, project):
        assert type(project.deadline) == int

    def test_get_backers_count(self, project):
        assert type(project.backers_count) == int
