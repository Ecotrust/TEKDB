# Generated by Django 3.2.11 on 2022-04-29 18:36

import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Configuration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('preferredInitialism', models.CharField(default='ITK', max_length=15, verbose_name='What to call this data: ITK? TEK?')),
                ('geometry', django.contrib.gis.db.models.fields.GeometryField(blank=True, default=None, help_text="Indicate the region in which most of your 'place' records are likely exist. This serves to set the map conveniently for staff entering records. Records are allowed to exist outside of the area you indicate, and this can be changed at any time.", null=True, srid=3857, verbose_name='Area of Interest')),
                ('homepageImage', models.ImageField(blank=True, default=None, help_text='If you have a preferred image for the landing page, put it here. If blank, users will see a default image.', upload_to='')),
            ],
        ),
    ]
