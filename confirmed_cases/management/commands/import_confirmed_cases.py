from django.core.management import BaseCommand
from django.contrib.gis.utils import LayerMapping

from confirmed_cases.models import ConfirmedCase


class Command(BaseCommand):
    help = "Import confirmed cases from shapefiles"

    def add_arguments(self, parser):
        parser.add_argument("shapefile", help="Path to the shapefile")

    def handle(self, *args, **options):
        shapefile = options["shapefile"]
        field_mapping = {
            "reported_date": "REPORTED_D",
            "reported_location": "POINT"
        }
        lm = LayerMapping(ConfirmedCase, shapefile, field_mapping)
        lm.save(verbose=True)