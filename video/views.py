from lib2to3.fixes.fix_input import context

from django.http import HttpResponse, HttpRequest
from django.shortcuts import render

from . import models


# Create your views here.

def video_page(req: HttpRequest) -> HttpResponse:
    video = models.Video.objects.get(pk=1)
    context = {'video': video}
    return render(req, "video/video.html", context)