from django.shortcuts import render, redirect
from .forms import RegistrationForm
from django.contrib.auth import authenticate, login

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('success.html')
        else:
            return render(request, 'login_page.html', {'error_message': 'Invalid login'})
    else:
        return render(request, 'login_page.html')


def registration_view(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = RegistrationForm()
    return render(request, 'registration/registration.html', {'form': form})