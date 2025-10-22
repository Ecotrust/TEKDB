from django.core.management.base import BaseCommand
import os
# from TEKDB.models import *
# from TEKDB.settings import *


class Command(BaseCommand):
    help = "Imports spatial data from a separate PostGIS database with schema matching old db"

    def add_arguments(self, parser):
        parser.add_argument("infile", nargs="+", type=str)

    def handle(self, *args, **options):
        from django.contrib.gis.gdal import DataSource
        from pytz import timezone
        from datetime import datetime

        FILE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        MANAGE_DIR = os.path.join(FILE_DIR, "..", "..")
        infile = os.path.normpath(os.path.join(MANAGE_DIR, options["infile"][0]))
        if not os.path.exists(infile):
            print("File not found: %s" % infile)
            quit()
        if not infile[-4:] == ".shp":
            print('Please provide shapefile name ending in ".shp".')
            quit()

        try:
            ds = DataSource(infile)
            layer = ds[0]
            # TODO: Can we detect the srs and convert to 3857 on the fly?
            print("SRID: %s" % layer.srs.srid)
            fields = layer.fields

            if "PlaceID" not in fields:
                print(
                    "This is not a valid shapefile - no PlaceID field found. Available given: %s"
                    % str(fields)
                )
                quit()

            from TEKDB.models import (
                Places,
                Locality,
                LookupHabitat,
                LookupLocalityType,
            )

            if "LocalityID" in fields:
                model = Locality
                pk_field = "LocalityID"
                label_field = "LocalityLa"
                description_field = "LocalityDe"
            else:
                model = Places
                pk_field = "PlaceID"
                label_field = "PlaceLabel"
                description_field = "PlaceDescr"

            for geom_index, feature in enumerate(layer.get_geoms()):
                pk = layer.get_fields(pk_field)[geom_index]
                try:
                    (record, created) = model.objects.get_or_create(pk=pk)
                    from TEKDB.settings import TIME_ZONE

                    local_tz = timezone(TIME_ZONE)
                    record_date = local_tz.localize(
                        datetime.combine(
                            layer.get_fields("DigitizedD")[geom_index],
                            datetime.min.time(),
                        )
                    )
                    if created:
                        print(
                            "No DB record for %s (ID: %s) found. Creating a new one..."
                            % (layer.get_fields(label_field)[geom_index], str(pk))
                        )
                        if model == Locality:
                            place = Places.objects.filter(
                                pk=layer.get_fields("PlaceID")[geom_index]
                            )
                            if len(place) == 1:
                                record.placeid = place[0]
                            record.englishname = layer.get_fields(label_field)[
                                geom_index
                            ]
                            record.indigenousname = layer.get_fields(label_field)[
                                geom_index
                            ]
                            (localitytype, lt_created) = (
                                LookupLocalityType.objects.get_or_create(
                                    localitytype__iexact=layer.get_fields("FeatType")[
                                        geom_index
                                    ]
                                )
                            )
                            if lt_created:
                                localitytype.localitytype = layer.get_fields(
                                    "FeatType"
                                )[geom_index]
                                localitytype.save()
                                print(
                                    "Created Locality Type: %s (ID: %s)"
                                    % (localitytype.localitytype, localitytype.id)
                                )
                            record.localitytype = localitytype
                        else:
                            record.indigenousplacename = layer.get_fields(label_field)[
                                geom_index
                            ]
                            record.indigenousplacenamemeaning = layer.get_fields(
                                description_field
                            )[geom_index]
                            record.englishplacename = layer.get_fields(label_field)[
                                geom_index
                            ]
                            (habitat, hab_created) = (
                                LookupHabitat.objects.get_or_create(
                                    habitat__iexact=layer.get_fields("FeatType")[
                                        geom_index
                                    ]
                                )
                            )
                            if hab_created:
                                habitat.habitat = layer.get_fields("FeatType")[
                                    geom_index
                                ]
                                habitat.save()
                                print(
                                    "Created Habitat: %s (ID: %s)"
                                    % (habitat.habitat, habitat.id)
                                )
                            record.primaryhabitat = habitat
                        record.enteredbyname = layer.get_fields("DigitizedB")[
                            geom_index
                        ]
                        record.enteredbydate = record_date
                        record.modifiedbyname = layer.get_fields("DigitizedB")[
                            geom_index
                        ]
                        record.modifiedbydate = record_date
                    record.geometry = feature.geos
                    record.Source = layer.get_fields("Source")[geom_index]
                    record.DigitizedBy = layer.get_fields("DigitizedB")[geom_index]
                    record.DigitizedDate = record_date
                    record.save()

                except:
                    print("Error editing %s record with ID: %s" % (model, str(pk)))

        except Exception:
            print(
                "An unexpected error occurred while trying to read the \
shapefile. Please be sure the shapefile exists as given in your \
arguments and that it is unzipped and has the Place or Locality \
data you wish to import and try again."
            )
            quit()
