# weather_project/urls.py
from django.contrib import admin
from django.urls import path, include
import debug_toolbar
from weather_proj import settings

urlpatterns = [
    path('__debug__/', include(debug_toolbar.urls)),
    path('admin/', admin.site.urls),
    path('', include('weather_app.urls')),  # Include weather_app URLs
]


