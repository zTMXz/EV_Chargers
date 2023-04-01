from django.shortcuts import render, redirect
from .models import Car, ServiceRequest, RentalRequest, RentalHistory, ServiceHistory
from .forms import ServiceRequestForm, RentalRequestForm
from django.views.generic import ListView, DetailView
from users.models import User

from datetime import datetime, timedelta


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
            service_request = form.save(commit=False)  # Создаем объект, но не сохраняем его в БД
            service_request.person = request.user  # Указываем пользователя в поле person
            service_request.save()

            car_model = service_request.car_model
            car = Car.objects.get(car_full_name=car_model)
            car.is_broken = True
            car.save()

            ServiceHistory.objects.create(user=request.user, car=car, description=service_request.description)

            return redirect('service_request_success')
    else:
        form = ServiceRequestForm()
    return render(request, 'EV_rent/service_request.html', {'form': form})


def service_request_success(request):
    return render(request, 'EV_rent/service_request_success.html')


def rental_request(request, car_id):
    car = Car.objects.get(pk=car_id)
    if request.method == 'POST':
        form = RentalRequestForm(request.POST)

        if form.is_valid():
            rental_request = form.save(commit=False)  # Создаем объект, но не сохраняем его в БД
            rental_request.person = request.user  # Указываем пользователя в поле person


            rental_request.car_model = car
            rental_request.save()

            car.is_rented = True
            car.save()

            RentalHistory.objects.create(user=request.user, car=car, start_date=datetime.now(), end_date=(datetime.now() + timedelta(days=rental_request.num_days)))

            return redirect('service_request_success')
    else:
        form = RentalRequestForm()
    return render(request, 'EV_rent/rental_request.html', {'form': form, 'car': car})


def rental_request_success(request):
    return render(request, 'EV_rent/service_request_success.html')
