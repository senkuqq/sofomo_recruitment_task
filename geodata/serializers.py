
from geodata.models import Geolocation
from rest_framework import serializers
from geodata.ipstack_client import IpstackClient


class GeolocationSerializer(serializers.HyperlinkedModelSerializer):
    ip_address = serializers.CharField(max_length=300, allow_blank=False, write_only=True)

    class Meta:
        model = Geolocation
        fields = '__all__'
        read_only_fields = tuple([f.name for f in Geolocation._meta.fields])

    def validate(self, attrs):
        client = IpstackClient()
        response = client.get_standard_lookup(attrs.get('ip_address'))
        attrs['ipstack_response'] = response
        if response.json().get('type') is None:
            raise serializers.ValidationError("Service returned empty IP type - probably you "
                                              "provided wrong IP or address!")
        if Geolocation.objects.filter(ip=response.json().get('ip')):
            raise serializers.ValidationError("This IP address already exists!")
        return attrs

    def create(self, validated_data):
        response = validated_data.get('ipstack_response').json()
        return Geolocation.objects.create(ip=response.get('ip'),
                                          type=response.get('type'),
                                          continent_code=response.get('continent_code'),
                                          continent_name=response.get('continent_name'),
                                          country_code=response.get('country_code'),
                                          country_name=response.get('country_name'),
                                          region_code=response.get('region_code'),
                                          region_name=response.get('region_name'),
                                          city=response.get('city'),
                                          zip=response.get('zip'),
                                          latitude=response.get('latitude'),
                                          longitude=response.get('longitude')
                                          )
