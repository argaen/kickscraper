import pytest
import kickscraper

from kickscraper import models


@pytest.fixture
def p():
    return models.Project(name="Mamma Coal-Reimagining Willie Nelson's Outlaw Concept Album")


@pytest.mark.main
class TestProject:

    def test_create(self):
        p = models.Project(name="Mamma Coal-Reimagining Willie Nelson's Outlaw Concept Album")
        assert type(p.connector) == kickscraper.backends.kickstarter.models.KickStarterProject

    def test_get_title(self, p):
        assert type(p.name) == str

    def test_get_id(self, p):
        assert type(p.id) == int

    def test_get_deadline(self, p):
        assert type(p.deadline) == int
