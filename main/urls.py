from django.urls import path
from django.urls import include

from main.views import home
from main.api import ConfigurationView
from rest_framework import routers

urlpatterns = [
    path('', home, name="home"),
]

api_router = routers.DefaultRouter()
# /api/main/configurations
api_router.register('configurations', ConfigurationView)

apiurls = ([
    # /api/main/<routers>
    path('', include(api_router.urls))
], 'main')
