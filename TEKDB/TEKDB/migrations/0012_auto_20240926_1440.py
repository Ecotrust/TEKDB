# Generated by Django 3.2.25 on 2024-09-26 21:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TEKDB', '0011_searchsettings'),
    ]

    operations = [
        migrations.AlterField(
            model_name='searchsettings',
            name='min_search_rank',
            field=models.FloatField(default=0.01, help_text='Weight 0-1 representing the minimum search rank threshold for search results.', verbose_name='Minimum Search Rank'),
        ),
        migrations.AlterField(
            model_name='searchsettings',
            name='min_search_similarity',
            field=models.FloatField(default=0.1, help_text='Weight 0-1 representing the minimum threshold for similar search results to be included in results.', verbose_name='Minimum Search Similarity'),
        ),
    ]