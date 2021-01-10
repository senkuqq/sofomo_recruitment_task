import django_filters
from django.db.migrations import serializer
from django.shortcuts import render

# Create your views here.
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters

from geodata.models import Geolocation
from rest_framework import viewsets
from rest_framework import permissions
from geodata.serializers import GeolocationSerializer


class GeolocationViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows geolocations to be viewed, created or deleted.
    """
    queryset = Geolocation.objects.all()
    serializer_class = GeolocationSerializer
    filter_backends = [filters.OrderingFilter, DjangoFilterBackend]
    ordering_fields = '__all__'
    filterset_fields = '__all__'
    permission_classes = [permissions.IsAuthenticated]
