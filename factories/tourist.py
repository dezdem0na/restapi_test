import factory
import factory.fuzzy

from random import randint
from django.contrib.auth.hashers import make_password
from apps.core.models import Country
from apps.tourist.models import Location, Visit, User

Faker = factory.Faker
DEFAULT_SUPERUSER_PASSWORD = 'password'


class UserFactory(factory.django.DjangoModelFactory):
    username = factory.Sequence(lambda n: f'username{n}')
    password = make_password(DEFAULT_SUPERUSER_PASSWORD)
    is_staff = False
    email = Faker('email')
    first_name = Faker('first_name')
    last_name = Faker('last_name')
    gender = factory.fuzzy.FuzzyChoice([1, 2])
    birth_date = Faker('date_this_century')
    country = Country()._get_random()

    class Meta:
        model = User

    @classmethod
    def _adjust_kwargs(cls, **kwargs):
        x = randint(0, 9999)
        kwargs['username'] = f"{kwargs['username']}{x}"
        return kwargs


class LocationFactory(factory.django.DjangoModelFactory):
    name = Faker('sentence')
    description = Faker('paragraph')
    country = Country()._get_random()
    city = Faker('city')

    class Meta:
        model = Location


class VisitFactory(factory.django.DjangoModelFactory):
    ratio = factory.fuzzy.FuzzyInteger(0, 10)
    date = Faker('past_datetime')
    location = factory.SubFactory(LocationFactory)
    user = factory.SubFactory(UserFactory)

    class Meta:
        model = Visit
