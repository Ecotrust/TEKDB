# Generated by Django 3.2.13 on 2023-01-20 19:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TEKDB', '0007_citations_rawcitation'),
    ]

    operations = [
        migrations.AddField(
            model_name='citations',
            name='date',
            field=models.DateField(blank=True, db_column='date', default=None, null=True),
        ),
    ]