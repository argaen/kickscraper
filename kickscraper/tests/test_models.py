import pytest
import kickscraper

from kickscraper import models


@pytest.fixture
def p():
    return models.Project(name="Mamma Coal-Reimagining Willie Nelson's Outlaw Concept Album")


def test_search_projects():
    d = kickscraper.search_projects(terms="Whatever")
    keys = ['total_hits', 'projects']
    subkeys = ['id', 'photo', 'name', 'goal', 'pledged', 'state', 'deadline', 'launched_at', 'backers_count', 'usd_pledged', 'creator', 'currency_symbol', 'launched_at']
    for k in keys:
        assert k in d
    for k in subkeys:
        assert k in d['projects'][0]


@pytest.mark.main
class TestProject:

    def test_create(self):
        p = models.Project(name="Mamma Coal-Reimagining Willie Nelson's Outlaw Concept Album")
        assert type(p.connector) == kickscraper.backends.kickstarter.models.KickStarterProject

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
