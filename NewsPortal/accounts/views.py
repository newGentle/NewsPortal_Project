from django.contrib.auth.models import User
from django.views.generic import CreateView
from .forms import CustomSignUpForm

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
