from django.db import models


class Geolocation(models.Model):
    ip = models.CharField(max_length=50)
    type = models.CharField(max_length=20)
    continent_code = models.CharField(max_length=2)
    continent_name = models.CharField(max_length=20)
    country_code = models.CharField(max_length=2)
    country_name = models.CharField(max_length=60)
    region_code = models.CharField(max_length=2)
    region_name = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    zip = models.CharField(max_length=15)
    latitude = models.DecimalField(max_digits=22, decimal_places=16)
    longitude = models.DecimalField(max_digits=22, decimal_places=16)
