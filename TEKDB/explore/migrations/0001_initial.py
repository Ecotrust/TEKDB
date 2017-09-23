# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-06-11 21:56
from __future__ import unicode_literals

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PageContent',
            fields=[
                ('page', models.CharField(choices=[('Welcome', 'Welcome'), ('About', 'About'), ('Help', 'Help')], max_length=255, primary_key=True, serialize=False)),
                ('is_html', models.BooleanField(default=False)),
                ('content', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('html_content', models.TextField(blank=True, help_text='raw html if html == True', null=True)),
            ],
        ),
    ]