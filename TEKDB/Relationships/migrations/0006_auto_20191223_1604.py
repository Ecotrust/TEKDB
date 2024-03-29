# -*- coding: utf-8 -*-
# Generated by Django 1.11.26 on 2019-12-24 00:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Relationships', '0005_auto_20191223_1538'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mediacitationevents',
            name='relationshipdescription',
            field=models.TextField(blank=True, db_column='relationshipdescription', null=True, verbose_name='excerpt/description'),
        ),
        migrations.AlterField(
            model_name='placescitationevents',
            name='relationshipdescription',
            field=models.TextField(blank=True, db_column='relationshipdescription', null=True, verbose_name='excerpt/description'),
        ),
        migrations.AlterField(
            model_name='placesmediaevents',
            name='relationshipdescription',
            field=models.TextField(blank=True, db_column='relationshipdescription', null=True, verbose_name='relationship description'),
        ),
        migrations.AlterField(
            model_name='placesresourcecitationevents',
            name='relationshipdescription',
            field=models.TextField(blank=True, db_column='relationshipdescription', null=True, verbose_name='excerpt/description'),
        ),
        migrations.AlterField(
            model_name='placesresourcemediaevents',
            name='relationshipdescription',
            field=models.TextField(blank=True, db_column='relationshipdescription', null=True, verbose_name='relationship description'),
        ),
        migrations.AlterField(
            model_name='resourceactivitymediaevents',
            name='relationshipdescription',
            field=models.TextField(blank=True, db_column='relationshipdescription', null=True, verbose_name='relationship description'),
        ),
        migrations.AlterField(
            model_name='resourcescitationevents',
            name='relationshipdescription',
            field=models.TextField(blank=True, db_column='relationshipdescription', null=True, verbose_name='excerpt/description'),
        ),
        migrations.AlterField(
            model_name='resourcesmediaevents',
            name='relationshipdescription',
            field=models.TextField(blank=True, db_column='relationshipdescription', null=True, verbose_name='relationship description'),
        ),
    ]
