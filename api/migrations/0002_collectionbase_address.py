# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-07-31 20:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='collectionbase',
            name='address',
            field=models.CharField(blank=True, default=None, max_length=200, null=True),
        ),
    ]
