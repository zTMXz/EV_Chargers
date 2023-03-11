import googlemaps
from django.conf import settings
from django.shortcuts import render

def map_view(request):
    gmaps = googlemaps.Client(key=settings.GOOGLE_MAPS_API_KEY)
    lat, lng = 37.4224764, -122.0842499  # координаты центра карты
    context = {'gmaps_api_key': settings.GOOGLE_MAPS_API_KEY,
               'lat': lat, 'lng': lng}
    return render(request, 'google_maps_ev/map.html', context)