from django.shortcuts import render, redirect
from .models import Car, ServiceRequest, RentalRequest
from .forms import ServiceRequestForm, RentalRequestForm


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
