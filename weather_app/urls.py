# weather_app/urls.py

from django.urls import path
from .views import register, search_weather, custom_login, get_weather_data, create_weather_data
from django.contrib.auth import views as auth_views

from django.contrib.auth.views import LoginView

urlpatterns = [

    path('', register, name='register'),
    path('login/', custom_login, name='login'),
    path('api/weather/', get_weather_data, name='get_weather_data'),
    path('api/weather/create/', create_weather_data, name='create_weather_data'),
    path('register/', register, name='register'),
    path('search_weather/', search_weather, name='search_weather'),
    path('logout/', auth_views.LogoutView.as_view(next_page='register'), name='logout')
]
