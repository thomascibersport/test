from django.urls import path
from . import views  # Импортируем views

urlpatterns = [
    path('', views.home_page),  # Домашняя страница
]


