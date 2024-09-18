from lib2to3.fixes.fix_input import context

from django.http import HttpResponse, HttpRequest
from django.shortcuts import render

from . import models


# Create your views here.

def video_page(req: HttpRequest, video_id: int) -> HttpResponse:
    video = models.Video.objects.get(pk=video_id)

    context = {'video': video}
    return render(req, "videos/video.html", context)