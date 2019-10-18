from django.urls import path, include

from main.views import home
from main.api import ConfigurationView
from rest_framework import routers

api_router = routers.DefaultRouter()
# /api/main/configuration
api_router.register('configurations', ConfigurationView)

apiurls = ([
    # /api/main/<routers>
    path('', include(api_router.urls))
], 'main')

urlpatterns = [
    path('', home, name="home"),
]
