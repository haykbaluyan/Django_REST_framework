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
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('name', models.CharField(blank=True, max_length=100, default='defName')),
                ('title', models.CharField(blank=True, max_length=1000, default='defTitle')),
                ('age', models.IntegerField(blank=True, max_length=5, default=0)),
            ],
        ),
    ]
