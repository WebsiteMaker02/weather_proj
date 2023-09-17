# weather_project/urls.py
from django.contrib import admin
from django.urls import path, include
from weather_proj import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('weather_app.urls')),  # Include weather_app URLs
]


