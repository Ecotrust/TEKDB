# Generated by Django 3.2.25 on 2024-10-22 23:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TEKDB', '0017_auto_20241016_1552'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mediabulkupload',
            name='mediabulkdate',
            field=models.DateField(blank=True, default=None, null=True, verbose_name='date'),
        ),
        migrations.AlterField(
            model_name='mediabulkupload',
            name='mediabulkdescription',
            field=models.TextField(blank=True, null=True, verbose_name='description'),
        ),
        migrations.AlterField(
            model_name='mediabulkupload',
            name='mediabulkname',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='name'),
        ),
    ]
