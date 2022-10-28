from django.shortcuts import render
from django.contrib.auth.models import User
from django.views.generic import CreateView
from .forms import CustomSignUpForm

# Create your views here.
class SignUp(CreateView):
    model = User
    form_class = CustomSignUpForm
    success_url = '/acounts/login'
    template_name = 'allauth/account/signup.html'