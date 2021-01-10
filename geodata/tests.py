import json

from django.contrib.auth.models import User
from django.test import TestCase
# Create your tests here.
from rest_framework.test import APIClient
import factory
from geodata.ipstack_client import IpstackClient
from geodata.models import Geolocation


class UserFactory(factory.Factory):
    class Meta:
        model = User


class TestGeolocation(TestCase):
    def setUp(self) -> None:
        self.client = APIClient()
        self.u1 = UserFactory()
        self.client.force_authenticate(user=self.u1)
        self.ip = '212.77.98.9' # wp.pl

    def test_ipstack_client(self):
        client = IpstackClient()

        response = client.get_standard_lookup(self.ip)
        self.assertTrue(response.status_code == 200, 'Wrong status code')
        self.assertIsNotNone(response.json().get('type'), 'Service returned empty type for ip {}'.format(self.ip))
        self.assertTrue(response.json().get('country_name') == 'Poland',
                        'Service returned wrong country for ip {}'.format(self.ip))

    def test_geolocation_creating(self):
        payload = {
            'ip_address': self.ip
        }
        x = self.client.post('/api/v1/geolocations/', data=json.dumps(payload), content_type='application/json')
        geolocation = Geolocation.objects.filter(ip = self.ip).first()
        self.assertTrue(geolocation.country_name == 'Poland',
                        'wrong country_name - {}, should be Poland'.format(geolocation.country_name))
