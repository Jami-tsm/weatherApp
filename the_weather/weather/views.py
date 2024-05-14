from django.shortcuts import render
import requests


# Create your views here.
def index(request):
    url = 'http://api.openweathermap.org/data/2.5/weather?q=las%20vegas&units=imperial&appid=f743a61e7ada3bf0669ed715de4d2e6f'
    city = 'Las Vegas'
    city_weather = requests.get(url.format(city)).json()
    weather = {
        'city': city,
        'temperature': city_weather['main']['temp'],
        'description': city_weather['weather'][0]['description'],
        'icon': city_weather['weather'][0]['icon']
    }
    context = {'weather':weather}
    return render(request, 'weather/index.html',context)