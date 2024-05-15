from django.shortcuts import render
import requests
from .models import City
from .forms import CityForm


# Create your views here.
def index(request):
    base_url = ('http://api.openweathermap.org/data/2.5/weather?q=&units=imperial&appid=f743a61e7ada3bf0669ed715de4d2e6f')

    cities = City.objects.all()

    if request.method == 'POST':
        form = CityForm(request.POST)
        if form.is_valid():
            form.save()

    form = CityForm()

    weather_data = []
    for city in cities:
        city_url = base_url.format(city.name)
        city_weather = requests.get(city_url).json()
        if city_weather.get('main') and city_weather.get('weather'):
            weather = {
                'city': city.name,
                'temperature': city_weather['main']['temp'],
                'description': city_weather['weather'][0]['description'],
                'icon': city_weather['weather'][0]['icon']
            }
            weather_data.append(weather)
        else:
            city.delete()

    context = {'weather_data': weather_data, 'form': form}
    return render(request, 'weather/index.html', context)
