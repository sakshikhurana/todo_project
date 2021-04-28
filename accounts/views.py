from django.shortcuts import render, reverse
from django.views.generic import CreateView
from django.contrib.auth.models import User
from .forms import SignUpForm
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import login, logout, authenticate
from django.utils import timezone
from django.contrib.auth.decorators import login_required
# Create your views here.


# class SignUpView(CreateView):
#     model = User
#     form_class = SignUpForm
#     template_name = 'accounts/registration.html'
#     success_url = 'home.html'


def signupuser(request):
    if request.method == 'GET':
        return render(request, 'accounts/registration.html', {'form': UserCreationForm()})
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(
                    request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('home')
            except IntegrityError:
                return render(request, 'accounts/registration.html', {'form': UserCreationForm(), 'error': 'That username has already been taken. Please choose a new username'})
        else:
            return render(request, 'accounts/registration.html', {'form': UserCreationForm(), 'error': 'Passwords did not match'})


def home_view(request):
    return render(request, 'home.html')
