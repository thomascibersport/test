from . import views
from django.urls import path

urlpatterns = [
    path('', views.video_page, name='video_page'),
]