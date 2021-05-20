from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

import basketapp.views as basketapp

app_name = 'basketapp'

urlpatterns = [
    path('', basketapp.basket, name='basket'),
    path('add/<pk>/', basketapp.basket_add, name='add'),
    path('remove/<pk>/', basketapp.basket_remove, name='remove'),
]
