from django.db import models
from django.utils import formats
from django.contrib.auth.models import AbstractUser
from django.core.validators import MaxValueValidator, MinValueValidator
from apps.tourist.choices import GENDER_CHOICES
from apps.core.models import Country


class User(AbstractUser):
    gender = models.PositiveSmallIntegerField(choices=GENDER_CHOICES,
                                              blank=True,
                                              null=True)
    birth_date = models.DateField(blank=True,
                                  null=True)
    country = models.ForeignKey(Country,
                                blank=True,
                                null=True)

    class Meta:
        ordering = ['id']

    def __str__(self):
        return f'{self.username}'


class Location(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    city = models.CharField(max_length=45)
    country = models.ForeignKey(Country)

    class Meta:
        ordering = ['id']

    def __str__(self):
        return f'{self.country} - {self.city}'


class Visit(models.Model):
    ratio = models.IntegerField(
        default=0,
        validators=[MaxValueValidator(10), MinValueValidator(0)]
    )
    date = models.DateTimeField()
    location = models.ForeignKey(Location,
                                 related_name='visits')
    user = models.ForeignKey(User,
                             related_name='visits')

    class Meta:
        ordering = ['id']

    def __str__(self):
        date = formats.date_format(self.date, "SHORT_DATETIME_FORMAT")
        return f'{date} {self.location}'
