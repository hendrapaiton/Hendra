from rest_framework import serializers
from shortener.models import Links

class URLSerializer(serializers.ModelSerializer):
    class Meta:
        model = Links
        fields = ['id', 'original_url', 'short_url']
