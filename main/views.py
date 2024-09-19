from django.http import HttpResponse, HttpRequest
from django.shortcuts import render

# Create your views here.

def home_page(req: HttpRequest) -> HttpResponse:
    return render(req, 'main/index.html')