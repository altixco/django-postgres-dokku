from django.db import models


class Configuration(models.Model):
    key = models.CharField(max_length=200)
    value = models.CharField(max_length=200)

    def __str__(self):
        return self.key
