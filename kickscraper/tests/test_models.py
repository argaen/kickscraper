import os
import json
import pytest

from kickscraper import models


def get_json_project():
    basepath = os.path.dirname(os.path.realpath(__file__))
    with open(os.path.join(basepath, 'fixtures', 'project1.json'), 'r') as f:
        return json.load(f)


@pytest.fixture(params=[
    (
        "Mamma Coal-Reimagining Willie Nelson's Outlaw Concept Album",
        'kickscraper.backends.kickstarter.models.KickStarterProject'
    ),
    (
        "project1.json",
        'kickscraper.backends.json.models.JsonProject'
    )
])
def p(request):
    return models.Project(name=request.param[0], backend=request.param[1])


@pytest.mark.main
class TestProject:

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
