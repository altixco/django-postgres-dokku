from django.contrib import admin
from main.models import Configuration


@admin.register(Configuration)
class ConfigurationAdmin(admin.ModelAdmin):
    list_display = ["key", "value"]
