import pytest

from rest_framework.test import APIClient
from django.core.management import call_command


pytest_plugins = [
    'fixtures.tourist',
]


@pytest.fixture(scope='session', autouse=True)
def django_db_setup(django_db_setup, django_db_blocker):
    with django_db_blocker.unblock():
        print('loading fixtures')
        call_command('loaddata', 'fixtures/countries')
        print('loading dummy data')
        call_command('dummydata')


@pytest.fixture
def api_client():
    """Anonymous client for REST API."""
    client = APIClient()
    return client


def pytest_sessionfinish(session, exitstatus):
    """Whole test run finishes. """
    print('pytest finish: cleanup')
