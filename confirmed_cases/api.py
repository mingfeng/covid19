from rest_framework_gis.serializers import GeoFeatureModelSerializer
from rest_framework.generics import ListAPIView

from confirmed_cases.models import ConfirmedCase


class ConfirmedCaseSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = ConfirmedCase
        geo_field = "reported_location"
        fields = ("id", "reported_date")


class ConfirmedCaseListView(ListAPIView):
    queryset = ConfirmedCase.objects.all()
    serializer_class = ConfirmedCaseSerializer