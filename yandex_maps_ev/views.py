from django.shortcuts import render
from EV_chargers.settings import YANDEX_MAPS_API_KEY as api_key

def yandex_maps(request):
    return render(request, 'yandex_maps_ev/map_ya.html', context={'api_key': api_key})