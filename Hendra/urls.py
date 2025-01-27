from django.urls import include, path
import shortener.urls
from shortener.views import IndexView, URLRedirectView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('url/<str:short_url>/', URLRedirectView.as_view(), name='url-redirect'),
    path('api/', include(shortener.urls))
]
