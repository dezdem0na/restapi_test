from django.contrib import admin
from apps.core.models import Country


@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    pass
