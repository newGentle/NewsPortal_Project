from django.shortcuts import render
from django.contrib.auth.models import User
from django.views.generic import CreateView
from django.views import View
from .forms import CustomSignUpForm
from news.models import Category



# Create your views here.
class SignUp(CreateView):
    model = User
    form_class = CustomSignUpForm
    success_url = '/accounts/login'
    template_name = 'allauth/account/signup.html'

class LoginView(CreateView):
    model = User
    form_class = CustomSignUpForm
    success_url = 'posts_list'

