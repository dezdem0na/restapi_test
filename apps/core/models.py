from random import randint
from django.db import models
from django.db.models import Count


class Country(models.Model):
    name = models.CharField(max_length=45)

    class Meta:
        verbose_name = 'Country'
        verbose_name_plural = 'Countries'
        ordering = ('name',)

    def __str__(self):
        return f'{self.name}'

    def _get_random(self):
        count = self._meta.model.objects.aggregate(count=Count('pk'))['count']
        random_index = randint(0, count - 1)
        return self._meta.model.objects.get(pk=random_index)
