from . import views
from django.urls import path
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.video, name='video'),
    path('<int:video_id>/', views.video_page, name='video_page'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
]