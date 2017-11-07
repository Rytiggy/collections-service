# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-11-06 18:21
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_auto_20171106_1529'),
    ]

    operations = [
        migrations.AlterField(
            model_name='collectiongroup',
            name='collection',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='collection_groups', to='api.Collection'),
        ),
        migrations.AlterField(
            model_name='collectiongroup',
            name='group',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='collection_groups', to='auth.Group'),
        ),
    ]