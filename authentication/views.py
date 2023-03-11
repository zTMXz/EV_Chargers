# from django.contrib.auth import authenticate, login
# from django.shortcuts import render, redirect
# from .forms import LoginForm
#
# def login_view(request):
#     if request.method == 'POST':
#         form = LoginForm(request.POST)
#         if form.is_valid():
#             email = form.cleaned_data.get('username')
#             password = form.cleaned_data.get('password')
#             user = authenticate(request, username=email, password=password)
#             if user is not None:
#                 login(request, user)
#                 return redirect('admin')
#     else:
#         form = LoginForm()
#     return render(request, 'authentication/login_page.html', {'form': form})


from django.shortcuts import render, redirect
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
