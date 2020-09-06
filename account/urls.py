# -*- coding: utf-8 -*-
from django.urls import path

from . import views

app_name = "account"
urlpatterns = [
    path('register/', view=views.UserRegisterView.as_view(), name='register'),
]