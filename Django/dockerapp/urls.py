from django.urls import path
from . import views

urlpatterns = [
    path('', views.docker, name='docker'),
]