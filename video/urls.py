from . import views
from django.urls import path


urlpatterns = [
    path('<int:video_id>', views.video_page),
]