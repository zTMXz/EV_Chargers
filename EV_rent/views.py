from django.shortcuts import render, redirect
from .models import Car, ServiceRequest, RentalRequest
from .forms import ServiceRequestForm, RentalRequestForm
from django.views.generic.base import View
from django.views.generic import ListView, DetailView


class CarList(ListView):
    model = Car
    queryset = Car.objects.all()
    # здесь template_name = "EV_rent/car_list.html" по умолчанию, так как django ищет html с ИМЯ-МОДЕЛИ_list.html
    context_object_name = "cars"

class ModelDetailView(DetailView):
    model = Car
    slug_field = "url_page"
    # здесь template_name = "EV_rent/car_detail.html" по умолчанию, так как django ищет html с ИМЯ-МОДЕЛИ_detail.html


def service_request(request):
    if request.method == 'POST':
        form = ServiceRequestForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()

            model = " ".join(str(form.cleaned_data.get('car_model')).split()[1:])
            car = Car.objects.get(model=model)
            car.is_broken = True
            car.save()

            return redirect('service_request_success')
    else:
        form = ServiceRequestForm()
    return render(request, 'EV_rent/service_request.html', {'form': form})


def service_request_success(request):
    return render(request, 'EV_rent/service_request_success.html')


def rental_request(request):
    if request.method == 'POST':
        form = RentalRequestForm(request.POST)
        if form.is_valid():
            form.save()

            model = " ".join(str(form.cleaned_data.get('car_model')).split()[1:])
            rent = RentalRequest.objects.get(car_model=form.cleaned_data.get('car_model'))
            car = Car.objects.get(model=model)
            car.is_rented = True
            rent.is_rented = True
            car.save()
            rent.save()

            return redirect('service_request_success')
    else:
        form = RentalRequestForm()
    return render(request, 'EV_rent/rental_request.html', {'form': form})


def rental_request_success(request):
    return render(request, 'EV_rent/service_request_success.html')
