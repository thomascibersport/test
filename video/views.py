from django.http import HttpResponse, HttpRequest
from django.shortcuts import render

# Create your views here.

def video_page(req: HttpRequest) -> HttpResponse:
    return HttpResponse("This is video")