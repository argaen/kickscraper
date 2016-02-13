import pytest
import kickscraper

from kickscraper import models


@pytest.fixture
def p():
    return models.Project(uid=1946925378, name="Mamma Coal-Reimagining Willie Nelson's Outlaw Concept Album")


@pytest.mark.main
class TestProject:

    def test_create(self):
        p = models.Project(uid=1946925378, name="Mamma Coal-Reimagining Willie Nelson's Outlaw Concept Album")
        assert type(p.connector) == kickscraper.backends.kickstarter.models.KickStarterProject

    def test_get_title(self, p):
        assert type(p.title) == str

    def test_get_time_to_go(self, p):
        assert type(p.time_to_go) == int
