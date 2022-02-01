from os import name
from django.urls import path
from .views import *

urlpatterns = [
    path('',index),
    path('car/',car, name='car'),
    path('order/', order, name='order'),
]