from rest_framework import generics
from django.views.generic import TemplateView
from django.shortcuts import get_object_or_404, redirect

from shortener.models import Links
from shortener.serializers import URLSerializer

class URLCreateView(generics.CreateAPIView):
    queryset = Links.objects.all()
    serializer_class = URLSerializer

class URLRetrieveView(generics.RetrieveAPIView):
    queryset = Links.objects.all()
    serializer_class = URLSerializer
    lookup_field = 'short_url'

class URLRedirectView(TemplateView):
    def get(self, request, short_url, *args, **kwargs):
        link = get_object_or_404(Links, short_url=short_url)
        return redirect(link.original_url)

class IndexView(TemplateView):
    template_name = "index.html"
