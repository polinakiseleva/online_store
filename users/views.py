from django.contrib.auth.views import LoginView as MyLoginView, LogoutView as MyLogoutView


class LoginView(MyLoginView):
    template_name = 'users/login.html'


class LogoutView(MyLogoutView):
    template_name = 'users/login.html'
