from django.contrib.gis import admin

from confirmed_cases.models import ConfirmedCase

HELSINKI_LONGITUDE = 2776957.204335059
HELSINKI_LATITUDE = 8442622.403718097


@admin.register(ConfirmedCase)
class ConfirmedCaseAdmin(admin.OSMGeoAdmin):
    list_display = ("id", "reported_date", "reported_location")
    default_lat = HELSINKI_LATITUDE
    default_lon = HELSINKI_LONGITUDE
    map_width = 800
    map_height = 600
    default_zoom = 12
