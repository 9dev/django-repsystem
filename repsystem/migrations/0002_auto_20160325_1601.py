# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('repsystem', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reputation',
            name='id',
        ),
        migrations.AlterField(
            model_name='reputation',
            name='user',
            field=models.OneToOneField(primary_key=True, to=settings.AUTH_USER_MODEL, serialize=False),
        ),
    ]
