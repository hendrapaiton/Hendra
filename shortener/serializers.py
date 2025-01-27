from rest_framework import serializers
from shortener.models import Links
from django.conf import settings

class URLSerializer(serializers.ModelSerializer):
    full_short_url = serializers.SerializerMethodField()

    class Meta:
        model = Links
        fields = ['id', 'original_url', 'short_url', 'full_short_url']

    def get_full_short_url(self, obj):
        return f"{settings.ROOT_URL}/{obj.short_url}"
