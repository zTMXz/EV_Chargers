from django.shortcuts import render

def yandex_maps(request):
    return render(request, 'yandex_maps_ev/map_ya.html')