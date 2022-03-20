from django.contrib import admin
from django.urls import path
from app.views import Home, Create, Store, Painel, Login, dashboard

urlpatterns = [
    path('', Home),
    path('create/', Create),
    path('store/', Store),
    path('painel/', Painel),
    path('login/', Login),
    path('dashboard/', dashboard),
]
