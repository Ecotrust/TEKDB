# Generated by Django 3.2.25 on 2024-09-27 22:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('configuration', '0009_configuration_preferredinitialismplacement'),
    ]

    operations = [
        migrations.AlterField(
            model_name='configuration',
            name='preferredInitialismPlacement',
            field=models.CharField(choices=[('default', 'Default'), ('before', 'Before'), ('after', 'After')], default=('default', 'Default'), help_text='Select the position of the preferred initialism in relative to the logo.', max_length=255),
        ),
    ]