from django.shortcuts import render
from django.views.generic import CreateView
from .forms import *
# Create your views here.


class RegisterView(CreateView):
    template_name = 'allauth/account/signup.html'
    form_class = RegisterForm
    success_url = '/'
