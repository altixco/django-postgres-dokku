from main.models import Configuration
from main.serializer import ConfigurationSerializer
from rest_framework import viewsets, permissions


class ConfigurationView(viewsets.ReadOnlyModelViewSet):
    permission_classes = [permissions.AllowAny]
    queryset = Configuration.objects.all()
    serializer_class = ConfigurationSerializer
