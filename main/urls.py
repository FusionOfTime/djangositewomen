from django.contrib import admin
from django.urls import path, re_path, register_converter
from . import views
from . import converters

register_converter(converters.FourDigitYearConverter, "year4")

urlpatterns = [
    path('', views.MainPage), # http://127.0.0.1:8000
    path('cats/<int:cat_id>/', views.categories),  # http://127.0.0.1:8000/cats/1
    path('cats/<slug:cat_slug>/', views.categories_by_slug),  # http://127.0.0.1:8000/cats/fssss
    path("archive/<year4:year>/", views.archive)

]
