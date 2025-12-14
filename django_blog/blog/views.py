# blog/views.py
from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView
from .forms import RegistrationForm
from django.contrib.auth import login

def home(request):
    return render(request, 'blog/home.html')

def posts(request):
    return render(request, 'blog/posts.html')

class UserLoginView(LoginView):
    template_name = 'blog/login.html'

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = RegistrationForm()
    return render(request, 'blog/register.html', {'form': form})
