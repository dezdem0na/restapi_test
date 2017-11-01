import pytest


@pytest.fixture()
def location(django_db_blocker):
    with django_db_blocker.unblock():
        from factories.tourist import LocationFactory
        _location = LocationFactory()
        return _location


@pytest.fixture()
def user(django_db_blocker):
    with django_db_blocker.unblock():
        from factories.tourist import UserFactory
        _user = UserFactory()
        return _user


@pytest.fixture()
def visit(django_db_blocker):
    with django_db_blocker.unblock():
        from factories.tourist import VisitFactory
        _visit = VisitFactory()
        return _visit


@pytest.fixture()
def user_with_ratio(django_db_blocker):
    with django_db_blocker.unblock():
        from factories.tourist import VisitFactory
        from factories.tourist import UserFactory
        from factories.tourist import LocationFactory
        _user = UserFactory()
        _location = LocationFactory()
        _visit = VisitFactory(location=_location,
                              user=_user,
                              ratio=9)
        return _user


@pytest.fixture()
def location_with_ratio(django_db_blocker):
    with django_db_blocker.unblock():
        from factories.tourist import VisitFactory
        from factories.tourist import UserFactory
        from factories.tourist import LocationFactory
        _user = UserFactory()
        _location = LocationFactory()
        _visit = VisitFactory(location=_location,
                              user=_user,
                              ratio=8)
        return _location
