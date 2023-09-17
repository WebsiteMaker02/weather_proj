import requests
import logging
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.utils import timezone
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import WeatherSearch
from .serializers import WeatherSearchSerializer
from .forms import CustomRegistrationForm
from django.conf import settings
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render

accuweather_api_key = settings.WEATHER_API_KEY
location_endpoint = 'http://dataservice.accuweather.com/locations/v1/cities/search'

# Configure logging
logger = logging.getLogger(__name__)


def register(request):
    if request.method == 'POST':
        form = CustomRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()

            # Assign the 'User' role to the newly registered user
            user.groups.add(Group.objects.get(name='User'))
            return redirect('login')
    else:
        form = CustomRegistrationForm()
    return render(request, 'register.html', {'form': form})


def custom_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        logger.info(f"Username: {username}")
        logger.info(f"Password: {password}")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            logger.info("Login successful")
            return redirect('search_weather')
        else:
            messages.error(request, 'Invalid username or password.')
            logger.error("Authentication failed")
    return render(request, 'login.html')


def search_weather(request):
    error_message = ''
    location = ''
    weather_data = None
    print(accuweather_api_key)
    print(location_endpoint)
    if request.method == 'POST':
        location = request.POST.get('location')
        if location:

            params = {
                'apikey': accuweather_api_key,
                'q': location,
            }

            response = requests.get(location_endpoint, params=params)
            print(response.status_code)
            if response.status_code == 200:
                data = response.json()
                print(data)
                if data:
                    location_key = data[0]['Key']

                    if location_key:
                        weather_endpoint = f'http://dataservice.accuweather.com/currentconditions/v1/{location_key}'
                        params = {
                            'apikey': accuweather_api_key,
                        }
                        response = requests.get(weather_endpoint, params=params)
                        if response.status_code == 200:
                            weather_data = response.json()
                            if weather_data:
                                observation_time = weather_data[0].get('LocalObservationDateTime', '')
                                weather_text = weather_data[0].get('WeatherText', '')
                                temperature_metric = weather_data[0].get('Temperature', {}).get('Metric', {}).get(
                                    'Value', 0)

                                WeatherSearch.objects.create(
                                    location=location,
                                    temperature=temperature_metric,
                                    weather_condition=weather_text,
                                    searched_at=timezone.now(),
                                )
                        else:
                            error_message = 'Error fetching weather data. Please try again.'
                else:
                    error_message = 'No weather data found for the specified location. Please try again'
            else:
                error_message = 'Error fetching weather data. Please try again.'
        else:
            error_message = 'Location cannot be empty.'

    return render(request, 'search.html',
                  {'error_message': error_message, 'weather_data': weather_data, 'location': location})


@api_view(['GET'])
def get_weather_data(request):
    weather_data = WeatherSearch.objects.all()
    serializer = WeatherSearchSerializer(weather_data, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def create_weather_data(request):
    serializer = WeatherSearchSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)





def is_admin(user):
    return user.groups.filter(name='Admin').exists()



@user_passes_test(is_admin)
def admin_page(request):
    # Your admin page logic here
    return render(request, 'admin_page.html')
