from django.contrib.auth import authenticate, login
from django.core.mail import send_mail, BadHeaderError
from django.shortcuts import render, redirect
from django.views import View

from EV_chargers.settings import DEFAULT_FROM_EMAIL
from users.forms import UserCreationForm


class Register(View):
    template_name = 'registration/register.html'

    def get(self, request):
        context = {
            'form': UserCreationForm()
        }
        return render(request, self.template_name, context)

    def post(self, request):
        form = UserCreationForm(request.POST)


        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            email = form.cleaned_data.get('email')
            user = authenticate(username=username, password=password)
            login(request, user)

            #РАБОТАЕТ, ПОТОМ ПЕРЕПИСАТЬ
            send_mail(subject='registration',
                      message='thx for reg',
                      recipient_list=[email],
                      from_email=DEFAULT_FROM_EMAIL
                      )

            return redirect('home')



        context = {
            'form': form
        }
        return render(request, self.template_name, context)

