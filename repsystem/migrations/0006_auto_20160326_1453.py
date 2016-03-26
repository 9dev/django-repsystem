# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('repsystem', '0005_action'),
    ]

    operations = [
        migrations.AlterField(
            model_name='action',
            name='name',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
