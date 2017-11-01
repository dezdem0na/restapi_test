from django.core.management.base import BaseCommand
from factories.tourist import UserFactory, VisitFactory, LocationFactory
from apps.core.models import Country


class Command(BaseCommand):
    help = 'Create dummy data'

    def add_arguments(self, parser):
        parser.add_argument('--number', nargs='+', type=int, default=[3])

    def handle(self, *args, **options):
        number = options['number'][0]

        for i in range(0, number):
            user = UserFactory()
            self.stdout.write(
                self.style.SUCCESS(f'[{__name__}] User {user.pk} created')
            )
            loc = LocationFactory(country=Country()._get_random())
            self.stdout.write(
                self.style.SUCCESS(f'[{__name__}] Location {loc.pk} created')
            )
            visit = VisitFactory(location=loc, user=user)
            self.stdout.write(
                self.style.SUCCESS(f'[{__name__}] Visit {visit.pk} created')
            )
