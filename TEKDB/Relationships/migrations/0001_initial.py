# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-13 23:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='LocalityGISSelections',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('localitylabel', models.CharField(blank=True, db_column='localitylabel', max_length=255, null=True, verbose_name='locality label')),
                ('sourcefc', models.CharField(blank=True, db_column='sourcefc', max_length=255, null=True, verbose_name='source fc')),
            ],
            options={
                'db_table': 'localitygisselections',
                'managed': True,
                'verbose_name_plural': 'Locality GIS Selections',
            },
        ),
        migrations.CreateModel(
            name='LocalityPlaceResourceEvent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('enteredbyname', models.CharField(blank=True, db_column='enteredbyname', max_length=25, null=True, verbose_name='entered by name')),
                ('enteredbytribe', models.CharField(blank=True, db_column='enteredbytribe', max_length=100, null=True, verbose_name='entered by tribe')),
                ('enteredbytitle', models.CharField(blank=True, db_column='enteredbytitle', max_length=100, null=True, verbose_name='entered by title')),
                ('enteredbydate', models.DateTimeField(auto_now_add=True, db_column='enteredbydate', null=True, verbose_name='entered by date')),
                ('modifiedbyname', models.CharField(blank=True, db_column='modifiedbyname', max_length=25, null=True, verbose_name='modified by name')),
                ('modifiedbytitle', models.CharField(blank=True, db_column='modifiedbytitle', max_length=100, null=True, verbose_name='modified by title')),
                ('modifiedbytribe', models.CharField(blank=True, db_column='modifiedbytribe', max_length=100, null=True, verbose_name='modified by tribe')),
                ('modifiedbydate', models.DateTimeField(auto_now=True, db_column='modifiedbydate', null=True, verbose_name='modified by date')),
            ],
            options={
                'db_table': 'localityplaceresourceevent',
                'managed': True,
                'verbose_name_plural': 'Localities - Place-Resources',
            },
        ),
        migrations.CreateModel(
            name='MediaCitationEvents',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('enteredbyname', models.CharField(blank=True, db_column='enteredbyname', max_length=25, null=True, verbose_name='entered by name')),
                ('enteredbytribe', models.CharField(blank=True, db_column='enteredbytribe', max_length=100, null=True, verbose_name='entered by tribe')),
                ('enteredbytitle', models.CharField(blank=True, db_column='enteredbytitle', max_length=100, null=True, verbose_name='entered by title')),
                ('enteredbydate', models.DateTimeField(auto_now_add=True, db_column='enteredbydate', null=True, verbose_name='entered by date')),
                ('modifiedbyname', models.CharField(blank=True, db_column='modifiedbyname', max_length=25, null=True, verbose_name='modified by name')),
                ('modifiedbytitle', models.CharField(blank=True, db_column='modifiedbytitle', max_length=100, null=True, verbose_name='modified by title')),
                ('modifiedbytribe', models.CharField(blank=True, db_column='modifiedbytribe', max_length=100, null=True, verbose_name='modified by tribe')),
                ('modifiedbydate', models.DateTimeField(auto_now=True, db_column='modifiedbydate', null=True, verbose_name='modified by date')),
                ('relationshipdescription', models.CharField(blank=True, db_column='relationshipdescription', max_length=255, null=True, verbose_name='excerpt/description')),
                ('pages', models.CharField(blank=True, db_column='pages', max_length=255, null=True)),
            ],
            options={
                'db_table': 'mediacitationevents',
                'verbose_name_plural': 'Media - Sources',
                'verbose_name': 'Medium - Source',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='PlaceAltIndigenousName',
            fields=[
                ('altindigenousnameid', models.AutoField(db_column='altindigenousnameid', primary_key=True, serialize=False)),
                ('altindigenousname', models.CharField(blank=True, db_column='altindigenousname', max_length=255, null=True, verbose_name='alternate name')),
            ],
            options={
                'db_table': 'placealtindigenousname',
                'verbose_name': 'Place - Alternate Name',
                'managed': True,
                'verbose_name_plural': 'Places - Alternate Names',
            },
        ),
        migrations.CreateModel(
            name='PlaceGISSelections',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('placelabel', models.CharField(blank=True, db_column='placelabel', max_length=255, null=True, verbose_name='label')),
                ('sourcefc', models.CharField(blank=True, db_column='sourcefc', max_length=255, null=True, verbose_name='source fc')),
            ],
            options={
                'db_table': 'placegisselections',
                'managed': True,
                'verbose_name_plural': 'Place GIS Selections',
            },
        ),
        migrations.CreateModel(
            name='PlacesCitationEvents',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('enteredbyname', models.CharField(blank=True, db_column='enteredbyname', max_length=25, null=True, verbose_name='entered by name')),
                ('enteredbytribe', models.CharField(blank=True, db_column='enteredbytribe', max_length=100, null=True, verbose_name='entered by tribe')),
                ('enteredbytitle', models.CharField(blank=True, db_column='enteredbytitle', max_length=100, null=True, verbose_name='entered by title')),
                ('enteredbydate', models.DateTimeField(auto_now_add=True, db_column='enteredbydate', null=True, verbose_name='entered by date')),
                ('modifiedbyname', models.CharField(blank=True, db_column='modifiedbyname', max_length=25, null=True, verbose_name='modified by name')),
                ('modifiedbytitle', models.CharField(blank=True, db_column='modifiedbytitle', max_length=100, null=True, verbose_name='modified by title')),
                ('modifiedbytribe', models.CharField(blank=True, db_column='modifiedbytribe', max_length=100, null=True, verbose_name='modified by tribe')),
                ('modifiedbydate', models.DateTimeField(auto_now=True, db_column='modifiedbydate', null=True, verbose_name='modified by date')),
                ('relationshipdescription', models.CharField(blank=True, db_column='relationshipdescription', max_length=255, null=True, verbose_name='excerpt/description')),
                ('pages', models.CharField(blank=True, db_column='pages', max_length=255, null=True)),
            ],
            options={
                'db_table': 'placescitationevents',
                'verbose_name_plural': 'Places - Sources',
                'verbose_name': 'Place - Source',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='PlacesMediaEvents',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('enteredbyname', models.CharField(blank=True, db_column='enteredbyname', max_length=25, null=True, verbose_name='entered by name')),
                ('enteredbytribe', models.CharField(blank=True, db_column='enteredbytribe', max_length=100, null=True, verbose_name='entered by tribe')),
                ('enteredbytitle', models.CharField(blank=True, db_column='enteredbytitle', max_length=100, null=True, verbose_name='entered by title')),
                ('enteredbydate', models.DateTimeField(auto_now_add=True, db_column='enteredbydate', null=True, verbose_name='entered by date')),
                ('modifiedbyname', models.CharField(blank=True, db_column='modifiedbyname', max_length=25, null=True, verbose_name='modified by name')),
                ('modifiedbytitle', models.CharField(blank=True, db_column='modifiedbytitle', max_length=100, null=True, verbose_name='modified by title')),
                ('modifiedbytribe', models.CharField(blank=True, db_column='modifiedbytribe', max_length=100, null=True, verbose_name='modified by tribe')),
                ('modifiedbydate', models.DateTimeField(auto_now=True, db_column='modifiedbydate', null=True, verbose_name='modified by date')),
                ('relationshipdescription', models.CharField(blank=True, db_column='relationshipdescription', max_length=255, null=True, verbose_name='relationship description')),
                ('pages', models.CharField(blank=True, db_column='pages', max_length=50, null=True)),
            ],
            options={
                'db_table': 'placesmediaevents',
                'verbose_name_plural': 'Places - Media',
                'verbose_name': 'Place - Medium',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='PlacesResourceCitationEvents',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('enteredbyname', models.CharField(blank=True, db_column='enteredbyname', max_length=25, null=True, verbose_name='entered by name')),
                ('enteredbytribe', models.CharField(blank=True, db_column='enteredbytribe', max_length=100, null=True, verbose_name='entered by tribe')),
                ('enteredbytitle', models.CharField(blank=True, db_column='enteredbytitle', max_length=100, null=True, verbose_name='entered by title')),
                ('enteredbydate', models.DateTimeField(auto_now_add=True, db_column='enteredbydate', null=True, verbose_name='entered by date')),
                ('modifiedbyname', models.CharField(blank=True, db_column='modifiedbyname', max_length=25, null=True, verbose_name='modified by name')),
                ('modifiedbytitle', models.CharField(blank=True, db_column='modifiedbytitle', max_length=100, null=True, verbose_name='modified by title')),
                ('modifiedbytribe', models.CharField(blank=True, db_column='modifiedbytribe', max_length=100, null=True, verbose_name='modified by tribe')),
                ('modifiedbydate', models.DateTimeField(auto_now=True, db_column='modifiedbydate', null=True, verbose_name='modified by date')),
                ('relationshipdescription', models.CharField(blank=True, db_column='relationshipdescription', max_length=255, null=True, verbose_name='excerpt/description')),
                ('pages', models.CharField(blank=True, db_column='pages', max_length=255, null=True)),
            ],
            options={
                'db_table': 'placesresourcecitationevents',
                'managed': True,
                'verbose_name_plural': 'Place-Resources - Sources',
            },
        ),
        migrations.CreateModel(
            name='PlacesResourceEvents',
            fields=[
                ('enteredbyname', models.CharField(blank=True, db_column='enteredbyname', max_length=25, null=True, verbose_name='entered by name')),
                ('enteredbytribe', models.CharField(blank=True, db_column='enteredbytribe', max_length=100, null=True, verbose_name='entered by tribe')),
                ('enteredbytitle', models.CharField(blank=True, db_column='enteredbytitle', max_length=100, null=True, verbose_name='entered by title')),
                ('enteredbydate', models.DateTimeField(auto_now_add=True, db_column='enteredbydate', null=True, verbose_name='entered by date')),
                ('modifiedbyname', models.CharField(blank=True, db_column='modifiedbyname', max_length=25, null=True, verbose_name='modified by name')),
                ('modifiedbytitle', models.CharField(blank=True, db_column='modifiedbytitle', max_length=100, null=True, verbose_name='modified by title')),
                ('modifiedbytribe', models.CharField(blank=True, db_column='modifiedbytribe', max_length=100, null=True, verbose_name='modified by tribe')),
                ('modifiedbydate', models.DateTimeField(auto_now=True, db_column='modifiedbydate', null=True, verbose_name='modified by date')),
                ('placeresourceid', models.AutoField(db_column='placeresourceid', primary_key=True, serialize=False)),
                ('relationshipdescription', models.CharField(blank=True, db_column='relationshipdescription', max_length=255, null=True, verbose_name='excerpt')),
                ('barterresource', models.BooleanField(db_column='barterresource', default=False, verbose_name='barter resource?')),
                ('january', models.BooleanField(db_column='january', default=False)),
                ('february', models.BooleanField(db_column='february', default=False)),
                ('march', models.BooleanField(db_column='march', default=False)),
                ('april', models.BooleanField(db_column='april', default=False)),
                ('may', models.BooleanField(db_column='may', default=False)),
                ('june', models.BooleanField(db_column='june', default=False)),
                ('july', models.BooleanField(db_column='july', default=False)),
                ('august', models.BooleanField(db_column='august', default=False)),
                ('september', models.BooleanField(db_column='september', default=False)),
                ('october', models.BooleanField(db_column='october', default=False)),
                ('november', models.BooleanField(db_column='november', default=False)),
                ('december', models.BooleanField(db_column='december', default=False)),
                ('year', models.IntegerField(blank=True, db_column='year', null=True)),
                ('islocked', models.BooleanField(db_column='islocked', default=False, verbose_name='locked?')),
            ],
            options={
                'db_table': 'placesresourceevents',
                'verbose_name': 'Place - Resource',
                'managed': True,
                'verbose_name_plural': 'Places - Resources',
            },
        ),
        migrations.CreateModel(
            name='PlacesResourceMediaEvents',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('enteredbyname', models.CharField(blank=True, db_column='enteredbyname', max_length=25, null=True, verbose_name='entered by name')),
                ('enteredbytribe', models.CharField(blank=True, db_column='enteredbytribe', max_length=100, null=True, verbose_name='entered by tribe')),
                ('enteredbytitle', models.CharField(blank=True, db_column='enteredbytitle', max_length=100, null=True, verbose_name='entered by title')),
                ('enteredbydate', models.DateTimeField(auto_now_add=True, db_column='enteredbydate', null=True, verbose_name='entered by date')),
                ('modifiedbyname', models.CharField(blank=True, db_column='modifiedbyname', max_length=25, null=True, verbose_name='modified by name')),
                ('modifiedbytitle', models.CharField(blank=True, db_column='modifiedbytitle', max_length=100, null=True, verbose_name='modified by title')),
                ('modifiedbytribe', models.CharField(blank=True, db_column='modifiedbytribe', max_length=100, null=True, verbose_name='modified by tribe')),
                ('modifiedbydate', models.DateTimeField(auto_now=True, db_column='modifiedbydate', null=True, verbose_name='modified by date')),
                ('relationshipdescription', models.CharField(blank=True, db_column='relationshipdescription', max_length=255, null=True, verbose_name='relationship description')),
                ('pages', models.CharField(blank=True, db_column='pages', max_length=50, null=True)),
            ],
            options={
                'db_table': 'placesresourcemediaevents',
                'managed': True,
                'verbose_name_plural': 'Place-Resources - Media',
            },
        ),
        migrations.CreateModel(
            name='ResourceActivityCitationEvents',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('enteredbyname', models.CharField(blank=True, db_column='enteredbyname', max_length=25, null=True, verbose_name='entered by name')),
                ('enteredbytribe', models.CharField(blank=True, db_column='enteredbytribe', max_length=100, null=True, verbose_name='entered by tribe')),
                ('enteredbytitle', models.CharField(blank=True, db_column='enteredbytitle', max_length=100, null=True, verbose_name='entered by title')),
                ('enteredbydate', models.DateTimeField(auto_now_add=True, db_column='enteredbydate', null=True, verbose_name='entered by date')),
                ('modifiedbyname', models.CharField(blank=True, db_column='modifiedbyname', max_length=25, null=True, verbose_name='modified by name')),
                ('modifiedbytitle', models.CharField(blank=True, db_column='modifiedbytitle', max_length=100, null=True, verbose_name='modified by title')),
                ('modifiedbytribe', models.CharField(blank=True, db_column='modifiedbytribe', max_length=100, null=True, verbose_name='modified by tribe')),
                ('modifiedbydate', models.DateTimeField(auto_now=True, db_column='modifiedbydate', null=True, verbose_name='modified by date')),
                ('relationshipdescription', models.CharField(blank=True, db_column='relationshipdescription', max_length=255, null=True, verbose_name='excerpt/description')),
                ('pages', models.CharField(blank=True, db_column='pages', max_length=255, null=True)),
            ],
            options={
                'db_table': 'resourceactivitycitationevents',
                'managed': True,
                'verbose_name_plural': 'Activity - Sources',
            },
        ),
        migrations.CreateModel(
            name='ResourceActivityMediaEvents',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('enteredbyname', models.CharField(blank=True, db_column='enteredbyname', max_length=25, null=True, verbose_name='entered by name')),
                ('enteredbytribe', models.CharField(blank=True, db_column='enteredbytribe', max_length=100, null=True, verbose_name='entered by tribe')),
                ('enteredbytitle', models.CharField(blank=True, db_column='enteredbytitle', max_length=100, null=True, verbose_name='entered by title')),
                ('enteredbydate', models.DateTimeField(auto_now_add=True, db_column='enteredbydate', null=True, verbose_name='entered by date')),
                ('modifiedbyname', models.CharField(blank=True, db_column='modifiedbyname', max_length=25, null=True, verbose_name='modified by name')),
                ('modifiedbytitle', models.CharField(blank=True, db_column='modifiedbytitle', max_length=100, null=True, verbose_name='modified by title')),
                ('modifiedbytribe', models.CharField(blank=True, db_column='modifiedbytribe', max_length=100, null=True, verbose_name='modified by tribe')),
                ('modifiedbydate', models.DateTimeField(auto_now=True, db_column='modifiedbydate', null=True, verbose_name='modified by date')),
                ('relationshipdescription', models.CharField(blank=True, db_column='relationshipdescription', max_length=255, null=True, verbose_name='relationship description')),
                ('pages', models.CharField(blank=True, db_column='pages', max_length=50, null=True)),
            ],
            options={
                'db_table': 'resourceactivitymediaevents',
                'managed': True,
                'verbose_name_plural': 'Activity - Media',
            },
        ),
        migrations.CreateModel(
            name='ResourceAltIndigenousName',
            fields=[
                ('altindigenousnameid', models.AutoField(db_column='altindigenousnameid', primary_key=True, serialize=False)),
                ('altindigenousname', models.CharField(blank=True, db_column='altindigenousname', max_length=255, null=True, verbose_name='alt name')),
            ],
            options={
                'db_table': 'resourcealtindigenousname',
                'managed': True,
                'verbose_name_plural': 'Resource Alternative Names',
            },
        ),
        migrations.CreateModel(
            name='ResourceResourceEvents',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('enteredbyname', models.CharField(blank=True, db_column='enteredbyname', max_length=25, null=True, verbose_name='entered by name')),
                ('enteredbytribe', models.CharField(blank=True, db_column='enteredbytribe', max_length=100, null=True, verbose_name='entered by tribe')),
                ('enteredbytitle', models.CharField(blank=True, db_column='enteredbytitle', max_length=100, null=True, verbose_name='entered by title')),
                ('enteredbydate', models.DateTimeField(auto_now_add=True, db_column='enteredbydate', null=True, verbose_name='entered by date')),
                ('modifiedbyname', models.CharField(blank=True, db_column='modifiedbyname', max_length=25, null=True, verbose_name='modified by name')),
                ('modifiedbytitle', models.CharField(blank=True, db_column='modifiedbytitle', max_length=100, null=True, verbose_name='modified by title')),
                ('modifiedbytribe', models.CharField(blank=True, db_column='modifiedbytribe', max_length=100, null=True, verbose_name='modified by tribe')),
                ('modifiedbydate', models.DateTimeField(auto_now=True, db_column='modifiedbydate', null=True, verbose_name='modified by date')),
                ('relationshipdescription', models.CharField(blank=True, db_column='relationshipdescription', max_length=255, null=True, verbose_name='relationship description')),
            ],
            options={
                'db_table': 'resourceresourceevents',
                'managed': True,
                'verbose_name_plural': 'Resources - Resources',
            },
        ),
        migrations.CreateModel(
            name='ResourcesCitationEvents',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('enteredbyname', models.CharField(blank=True, db_column='enteredbyname', max_length=25, null=True, verbose_name='entered by name')),
                ('enteredbytribe', models.CharField(blank=True, db_column='enteredbytribe', max_length=100, null=True, verbose_name='entered by tribe')),
                ('enteredbytitle', models.CharField(blank=True, db_column='enteredbytitle', max_length=100, null=True, verbose_name='entered by title')),
                ('enteredbydate', models.DateTimeField(auto_now_add=True, db_column='enteredbydate', null=True, verbose_name='entered by date')),
                ('modifiedbyname', models.CharField(blank=True, db_column='modifiedbyname', max_length=25, null=True, verbose_name='modified by name')),
                ('modifiedbytitle', models.CharField(blank=True, db_column='modifiedbytitle', max_length=100, null=True, verbose_name='modified by title')),
                ('modifiedbytribe', models.CharField(blank=True, db_column='modifiedbytribe', max_length=100, null=True, verbose_name='modified by tribe')),
                ('modifiedbydate', models.DateTimeField(auto_now=True, db_column='modifiedbydate', null=True, verbose_name='modified by date')),
                ('relationshipdescription', models.CharField(blank=True, db_column='relationshipdescription', max_length=255, null=True, verbose_name='excerpt/description')),
                ('pages', models.CharField(blank=True, db_column='pages', max_length=255, null=True)),
            ],
            options={
                'db_table': 'resourcescitationevents',
                'verbose_name_plural': 'Resources - Sources',
                'verbose_name': 'Resource - Source',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='ResourcesMediaEvents',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('enteredbyname', models.CharField(blank=True, db_column='enteredbyname', max_length=25, null=True, verbose_name='entered by name')),
                ('enteredbytribe', models.CharField(blank=True, db_column='enteredbytribe', max_length=100, null=True, verbose_name='entered by tribe')),
                ('enteredbytitle', models.CharField(blank=True, db_column='enteredbytitle', max_length=100, null=True, verbose_name='entered by title')),
                ('enteredbydate', models.DateTimeField(auto_now_add=True, db_column='enteredbydate', null=True, verbose_name='entered by date')),
                ('modifiedbyname', models.CharField(blank=True, db_column='modifiedbyname', max_length=25, null=True, verbose_name='modified by name')),
                ('modifiedbytitle', models.CharField(blank=True, db_column='modifiedbytitle', max_length=100, null=True, verbose_name='modified by title')),
                ('modifiedbytribe', models.CharField(blank=True, db_column='modifiedbytribe', max_length=100, null=True, verbose_name='modified by tribe')),
                ('modifiedbydate', models.DateTimeField(auto_now=True, db_column='modifiedbydate', null=True, verbose_name='modified by date')),
                ('relationshipdescription', models.CharField(blank=True, db_column='relationshipdescription', max_length=255, null=True, verbose_name='relationship description')),
                ('pages', models.CharField(blank=True, db_column='pages', max_length=50, null=True)),
            ],
            options={
                'db_table': 'resourcesmediaevents',
                'verbose_name_plural': 'Resources - Media',
                'verbose_name': 'Resource - Medium',
                'managed': True,
            },
        ),
    ]
