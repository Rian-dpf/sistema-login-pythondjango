from django.contrib import admin
from django.urls import path
from app.views import Home, Create, Store

urlpatterns = [
    path('', Home),
    path('create/', Create),
    path('store/', Store),
]
