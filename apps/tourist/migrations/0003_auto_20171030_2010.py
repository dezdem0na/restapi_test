# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-30 20:10
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tourist', '0002_auto_20171030_1953'),
    ]

    operations = [
        migrations.AlterField(
            model_name='visit',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='visitors', to=settings.AUTH_USER_MODEL),
        ),
    ]
