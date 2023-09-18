# Weather Search Web App

**Table of Contents**

- [Project Scope](#project-scope)
- [Prerequisites](#prerequisites)
- [Getting Started](#getting-started)
- [API Endpoints](#api-endpoints)
- [Configuration](#configuration)


## Project Scope

The Weather Search Web App is a Django-based web application that allows users to search for weather information for a specified location. Users can register, log in, search for weather data, and view their search history.

### Features

- User Registration: Users can register for an account to access the weather search functionality.
- User Login: Registered users can log in to their accounts.
- Weather Search: Users can enter a location and retrieve current weather information.
- Search History: The app stores a history of weather searches for each user.
- RESTful API: Provides endpoints to retrieve and create weather data.

## Prerequisites

Before running the application, ensure you have the following dependencies installed:

- Python (3.6 or higher)
- Django (4.2)
- Requests 
Certainly, here's a single README.md file that combines the previous content:

## Getting Started

Follow these steps to set up and run the Weather Search Web App:

1. Clone the repository to your local machine:

2.Install the required Python packages:
		pip install -r requirements.txt
		
3.Create the database and apply migrations:
		python manage.py migrate
		
4.Create a superuser for accessing the Django admin panel:
	python manage.py createsuperuser
	
5.Start the development server:
python manage.py runserver
Access the web app in your browser at http://localhost:8000/.

PS you may need to comment out static storage declaration in SETTINGS.py for local run


Log in with the superuser account to access the admin panel at http://localhost:8000/admin/.

## API Endpoints
The app provides the following API endpoints:

GET /api/weather/: Retrieve a list of weather data.

POST /api/weather/: Create a new weather data entry.

You can access these endpoints by making HTTP requests.

## Configuration
API Key: To fetch weather data, you need to configure your AccuWeather API key in the settings.py file. Set the WEATHER_API_KEY variable with your API key.



