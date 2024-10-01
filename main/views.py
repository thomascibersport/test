from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
import logging

def home_page(request: HttpRequest) -> HttpResponse:
    return render(request, 'main/index.html')

def custom_404(request, exception):
    logging.error(f'404 Error: {request.path}')
    return render(request, 'main/404.html', status=404)
