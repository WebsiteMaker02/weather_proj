# weather_app/models.py

from django.db import models
from django.contrib.auth.models import Group


class WeatherSearch(models.Model):
    location = models.CharField(max_length=255)
    temperature = models.DecimalField(max_digits=5, decimal_places=2)
    weather_condition = models.CharField(max_length=255)
    searched_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.location



Group.objects.get_or_create(name='User')
Group.objects.get_or_create(name='Admin')
