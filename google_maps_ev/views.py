from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Search
from .forms import SearchForm

import folium
import geocoder

def index(request):
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('map')
    else:
        form = SearchForm()

    address = Search.objects.all().last()
    milka = Search.objects.all()
    location = geocoder.osm(address)
    lat = location.lat
    lng = location.lng
    country = location.country


    if lat == None or lng == None:
        address.delete()
        return HttpResponse('Your address input is invalid')

    #Create Map Object
    m = folium.Map(location=[lat, lng], zoom_start=8)

    for city in milka:
        location = geocoder.osm(city)
        lat = location.lat
        lng = location.lng
        ct = location.city
        folium.Marker([lat, lng], tooltip='Click for more', popup=f"{ct}").add_to(m)

    folium.Marker([lat, lng], tooltip='Click for more', popup=f"{country}").add_to(m)
    #Get HTML Representation of Map Object
    m = m._repr_html_()

    context = {
        'm': m,
        'form': form,
    }
    return render(request, 'google_maps_ev/map.html', context=context)


def yan(request):
    return render(request, 'google_maps_ev/map_ya.html')