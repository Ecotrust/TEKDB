# Generated by Django 3.2.25 on 2024-10-25 20:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('configuration', '0011_alter_configuration_preferredinitialismplacement'),
    ]

    operations = [
        migrations.AddField(
            model_name='configuration',
            name='min_search_rank',
            field=models.FloatField(blank=True, default=None, help_text='Weight 0-1 representing the minimum search rank threshold for search results.', null=True, verbose_name='Minimum Search Rank'),
        ),
        migrations.AddField(
            model_name='configuration',
            name='min_search_similarity',
            field=models.FloatField(blank=True, default=None, help_text='Weight 0-1 representing the minimum threshold for similar search results to be included in results.', null=True, verbose_name='Minimum Search Similarity'),
        ),
    ]
