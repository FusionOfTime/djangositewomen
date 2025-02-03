from django.http import HttpResponse
from django.shortcuts import render

def MainPage(request):
    return HttpResponse("Главная страница сайта Women")


def CatsPage(request):
    return HttpResponse("<h1>Статьи по категориям</h1>")
