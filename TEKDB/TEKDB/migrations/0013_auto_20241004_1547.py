# Generated by Django 3.2.25 on 2024-10-04 22:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Lookup', '0005_alter_lookupuserinfo_id'),
        ('TEKDB', '0012_auto_20240926_1440'),
    ]

    operations = [
        migrations.CreateModel(
            name='MediaBulkUpload',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('date', models.DateField(blank=True, default=None, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('user', models.ForeignKey(blank=True, db_column='user', default=None, null=True, on_delete=django.db.models.deletion.SET_DEFAULT, to='Lookup.lookupuserinfo', verbose_name='user')),
            ],
        ),
        migrations.AddField(
            model_name='media',
            name='mediauploadevent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='mediabulkupload', to='TEKDB.mediabulkupload'),
        ),
    ]