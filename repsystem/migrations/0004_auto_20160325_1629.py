# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('repsystem', '0003_auto_20160325_1628'),
    ]

    operations = [
        migrations.AlterField(
            model_name='level',
            name='name',
            field=models.CharField(unique=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='level',
            name='required_rep',
            field=models.IntegerField(unique=True),
        ),
    ]
