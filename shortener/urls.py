from django.urls import path
from .views import URLCreateView

urlpatterns = [
    path('url/', URLCreateView.as_view(), name='url-create'),
]
