# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-31 21:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Relationships', '0002_auto_20171013_1650'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resourceresourceevents',
            name='relationshipdescription',
            field=models.TextField(blank=True, db_column='relationshipdescription', null=True, verbose_name='relationship description'),
        ),
    ]
