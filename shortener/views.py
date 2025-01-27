from rest_framework import generics
from django.views.generic import TemplateView

from shortener.models import Links
from shortener.serializers import URLSerializer

class URLCreateView(generics.CreateAPIView):
    queryset = Links.objects.all()
    serializer_class = URLSerializer

class URLRetrieveView(generics.RetrieveAPIView):
    queryset = Links.objects.all()
    serializer_class = URLSerializer
    lookup_field = 'short_url'

class IndexView(TemplateView):
    template_name = "index.html"
