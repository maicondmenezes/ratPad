import pytest

from reports.tests.factories import EscolaFactory

@pytest.fixture(autouse=True)
def media_storage(settings, tmpdir):
    settings.MEDIA_ROOT = tmpdir.strpath

@pytest.fixture
def escola():
    return EscolaFactory()