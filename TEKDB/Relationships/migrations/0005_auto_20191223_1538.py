# -*- coding: utf-8 -*-
# Generated by Django 1.11.26 on 2019-12-23 23:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Relationships', '0004_auto_20171031_1525'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='resourcealtindigenousname',
            options={'managed': True, 'verbose_name': 'Resource Alternative Name', 'verbose_name_plural': 'Resource Alternative Names'},
        ),
        migrations.AlterField(
            model_name='resourceactivitycitationevents',
            name='relationshipdescription',
            field=models.TextField(blank=True, db_column='relationshipdescription', null=True, verbose_name='excerpt/description'),
        ),
    ]
