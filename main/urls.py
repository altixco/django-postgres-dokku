# general imports
from django.urls import path
from main.views import home
from main.views import send_push_notification, register_device

# api imports

# api urls

# general urls
urlpatterns = [
    path('', home, name="home"),
    path('register_device/', register_device),
    path('send_push_notification/', send_push_notification),
]
