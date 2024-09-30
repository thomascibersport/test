from django.http import HttpResponse, HttpRequest
from django.shortcuts import render, get_object_or_404, redirect

from . import models
from .forms import CommentForm


# Create your views here.

def video(req: HttpRequest) -> HttpResponse:
    videos = models.Video.objects.all()

    context = {'videos': videos}
    return render(req, "videos/video.html", context)

def video_page(request, video_id):
    video = get_object_or_404(models.Video, id=video_id)
    comments = video.comments.all()

    # Если запрос POST, пытаемся сохранить комментарий, если пользователь авторизован
    if request.method == 'POST':
        if request.user.is_authenticated:
            form = CommentForm(request.POST)
            if form.is_valid():
                comment = form.save(commit=False)
                comment.video = video
                comment.user = request.user
                comment.save()
                return redirect('video_page', video_id=video.id)
        else:
            return redirect('login/login.html')  # Перенаправить на страницу входа

    # Если запрос GET или пользователь не авторизован, просто отображаем видео и комментарии
    else:
        form = CommentForm()

    return render(request, 'videos/video_page.html', {'video': video, 'comments': comments, 'form': form})
