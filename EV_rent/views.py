from django.shortcuts import render, redirect
from .models import Car
from .forms import ServiceRequestForm


def car_list(request):
    cars = Car.objects.all()
    return render(request, 'EV_rent/car_list.html', {'cars': cars})


def get_model_info(request, model: str):
    car = Car.objects.get(url_page=model)
    return render(request, 'EV_rent/car_info.html', {'car': car})


def service_request(request):
    if request.method == 'POST':
        form = ServiceRequestForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('service_request_success')
    else:
        form = ServiceRequestForm()
    return render(request, 'EV_rent/service_request.html', {'form': form})


def service_request_success(request):
    return render(request, 'EV_rent/service_request_success.html')
