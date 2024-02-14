from django.views.generic import CreateView
from django.contrib.auth.views import LoginView
from django.contrib.auth import logout
from django.shortcuts import redirect

from users.forms import UserRegister, AuthUser
from django.urls import reverse_lazy


class Register(CreateView):
    form_class = UserRegister
    template_name = 'users/register.html'
    success_url = reverse_lazy('users:login')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Регистрация'
        return context


class LoginUser(LoginView):
    form_class = AuthUser
    template_name = 'users/auth.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Авторизация'
        return context

    def get_success_url(self):
        return reverse_lazy('app:tasks')


def LogoutUser(request):
    logout(request)
    return redirect('users:login')
