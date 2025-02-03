from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('', views.MainPage), # http://127.0.0.1:8000
    path('cats/', views.CatsPage)  # http://127.0.0.1:8000/cats/

]
