from rest_framework import generics
from .models import Links
from .serializers import URLSerializer

class URLCreateView(generics.CreateAPIView):
    queryset = Links.objects.all()
    serializer_class = URLSerializer

class URLRetrieveView(generics.RetrieveAPIView):
    queryset = Links.objects.all()
    serializer_class = URLSerializer
    lookup_field = 'short_url'
