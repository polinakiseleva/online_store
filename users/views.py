from django.contrib.auth.views import LoginView as MyLoginView, LogoutView as MyLogoutView
from django.urls import reverse_lazy
from django.views.generic import CreateView

from users.forms import UserRegisterForm
from users.models import User


class LoginView(MyLoginView):
    template_name = 'users/login.html'


class LogoutView(MyLogoutView):
    pass


class RegisterView(CreateView):
    model = User
    form_class = UserRegisterForm
    success_url = reverse_lazy('users:login')
    template_name = 'users/register.html'
