from django.urls import include
import shortener


urlpatterns = [
    '', include(shortener.urls)
]
