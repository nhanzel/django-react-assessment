from django.shortcuts import render
from django.views.generic import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy

from .forms import CreateUserForm

# Create your views here.
class UserRegisterView(CreateView):
    form_class = CreateUserForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')