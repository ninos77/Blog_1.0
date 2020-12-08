from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import CreateView
from .forms import *
# Create your views here.


class RegisterView(CreateView):
    template_name = 'users/register.html'
    form_class = RegisterForm
    success_url = '/'


class UserLoginView(LoginView):
    template_name = 'users/login.html'


class UserLogoutView(LogoutView):
    template_name = 'users/logout.html'
