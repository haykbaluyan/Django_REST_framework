# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Snippet',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('name', models.CharField(default='defName', max_length=100, blank=True)),
                ('title', models.CharField(default='defTitle', max_length=1000, blank=True)),
                ('age', models.IntegerField(default=0, max_length=5, blank=True)),
            ],
        ),
    ]
