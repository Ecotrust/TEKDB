from django.core import management
from django.core.management.base import BaseCommand, CommandError
from django.conf import settings
from datetime import datetime
import io
import os, sys
import shutil
from TEKDB.models import *
import tempfile
import zipfile


class Command(BaseCommand):
    help = "Exports current content of database to /tmp/"

    def handle(self, *args, **options):
        datestamp = datetime.now().strftime("%Y%m%d")
        outfile = "/tmp/{}_backup.zip".format(datestamp)
        os.chdir(os.path.join(settings.MEDIA_ROOT, ".."))
        relative_media_directory = settings.MEDIA_ROOT.split(os.path.sep)[-1]
        # media_paths = get_all_file_paths(relative_media_directory, cwd=os.getcwd())
        media_paths = []
        for root, directories, files in os.walk(relative_media_directory):
            for filename in files:
                # join the two strings in order to form the full filepath.
                filepath = os.path.join(root, filename)
                media_paths.append(filepath)

        try:
            with tempfile.TemporaryDirectory() as tmp_dir:
                # create filename
                dumpfile = "{}_backup.json".format(datestamp)
                dumpfile_location = os.path.join(tmp_dir, dumpfile)
                with open(dumpfile_location, "w") as of:
                    management.call_command("dumpdata", "--indent=2", stdout=of)
                # zip up:
                #   * Data Dump file
                #   * Media files
                with zipfile.ZipFile(outfile, "w") as zip:
                    zip.write(dumpfile_location, dumpfile)
                    for media_file in media_paths:
                        zip.write(media_file)

            print("Export complete. Find your file at: {}".format(outfile))

        except Exception as e:
            print("Unknown Error Exporting Data: {}".format(e))
