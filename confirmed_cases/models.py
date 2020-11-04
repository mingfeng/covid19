from django.contrib.gis.db import models
from django.conf import settings


class ConfirmedCase(models.Model):
    reported_date = models.DateField()
    reported_location = models.PointField(srid=settings.SRID)

    def __str__(self):
        return f"Confirmed case #{self.id}"
