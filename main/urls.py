# general imports
from django.urls import path
from main.views import home

# api imports

# api urls

# general urls
urlpatterns = [
    path('', home, name="home"),
]
