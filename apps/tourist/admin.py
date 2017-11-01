from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from apps.tourist.models import Visit, Location, User


admin.site.register(User, UserAdmin)


@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    pass


@admin.register(Visit)
class VisitAdmin(admin.ModelAdmin):
    pass
