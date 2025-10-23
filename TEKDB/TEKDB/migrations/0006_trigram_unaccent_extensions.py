from django.contrib.postgres.operations import TrigramExtension, UnaccentExtension
from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("TEKDB", "0005_auto_20211021_1607"),
    ]

    operations = [TrigramExtension(), UnaccentExtension()]
