from django.urls import include, path
import shortener.urls
from shortener.views import IndexView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('api/', include(shortener.urls))
]
