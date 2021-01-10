import requests
import json
from django.conf import settings

DOMAIN = 'http://api.ipstack.com/'


class IpstackClient():
    def __init__(self, token='520f30576b5e19729f8bf64ab51be738'):
        self.token = token

    def get_standard_lookup(self, ip_address):
        response = requests.get('{}{}?access_key={}'.format(DOMAIN, ip_address, self.token))
        return response


