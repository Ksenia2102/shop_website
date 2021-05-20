from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

import mainapp.views as mainapp

app_name = 'mainapp'

urlpatterns = [
    path('<pk>/', mainapp.products, name='category'),
    path('', mainapp.products, name='index'),

]
