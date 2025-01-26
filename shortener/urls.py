from django.urls import path
from .views import URLCreateView, URLRetrieveView

urlpatterns = [
    path('url/', URLCreateView.as_view(), name='url-create'),
    # path('url/<str:short_url>/', URLRetrieveView.as_view(), name='url-retrieve'),
]
