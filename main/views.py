from django.http import HttpResponse, HttpRequest
from django.shortcuts import render

# Create your views here.

def home_page(req: HttpRequest) -> HttpResponse:
    return HttpResponse("Универ - Старая общага - СМОТРЕТЬ БЕСПЛАТНО")