from django.shortcuts import render, redirect
from django.views.generic import CreateView
from django.contrib.auth import login ,logout
from django.contrib.auth.views import LoginView 
from users.forms import RegisterCustomUserForm
from django.contrib.auth.forms import AuthenticationForm


class RegisterUserView(CreateView):
    form_class = RegisterCustomUserForm
    template_name = 'users/register.html'
    def form_valid(self,form):
        user = form.save()
        login(self.request, user=user)
        return redirect('home')


class LoginUserView(LoginView):
    form_class = AuthenticationForm
    template_name = 'users/login.html'


def exit(request):
    logout(request)
    return redirect('home')