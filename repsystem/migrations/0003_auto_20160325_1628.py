# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('repsystem', '0002_auto_20160325_1601'),
    ]

    operations = [
        migrations.CreateModel(
            name='Level',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('required_rep', models.IntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='reputation',
            name='level',
            field=models.ForeignKey(to='repsystem.Level', default=1),
        ),
    ]
